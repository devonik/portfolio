---
title: "Nuxt 4 WebSockets Are Elegant. Here's Why They Break on Vercel."
description: A first-hand debugging story — Nuxt 4's native WebSocket API is the cleanest I've seen in a full-stack framework, but the Nitro Vercel preset never implements the upgrade handshake. Vercel supports WebSockets fine; Nuxt's adapter for it just doesn't exist yet.
date: 2026-07-13
image: /blog/nuxt-websockets-vercel-hero.png
minRead: 7
author:
  name: Niklas Grieger
  avatar:
    src: /profile.jpg
    alt: Niklas Grieger
---

I needed realtime notifications on [gospendl.com](https://gospendl.com), a Bitcoin price comparison site built with Nuxt 4 and deployed on Vercel. A backend crawl job collects products from shops, uploads them to Algolia, and once that's done, any user currently sitting on `/search` should immediately see a "N new results for X found" banner — no refresh needed.

Nuxt's WebSocket API looked like exactly the right tool. It turned out to be missing its Vercel adapter — the problem isn't that Vercel can't do WebSockets, it's that Nitro's Vercel preset doesn't implement the upgrade handshake yet.

## What Nuxt 4 Offers, and How Clean It Is

Nuxt 4 / Nitro 2.13 has native WebSocket support via `crossws`. The setup is genuinely minimal — no separate WebSocket server, no extra dependency, no client SDK bindings.

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  nitro: {
    experimental: { websocket: true },
  },
})
```

```ts
// server/routes/ws.ts
export const peers = new Set<{ send: (m: string) => void }>()

export default defineWebSocketHandler({
  open(peer) { peers.add(peer) },
  close(peer) { peers.delete(peer) },
})
```

Broadcasting from anywhere in the backend is just:

```ts
peers.forEach(p => p.send(JSON.stringify({ source: 'crawl.newData', meta: {...} })))
```

And on the frontend, with `@vueuse/core`:

```ts
const { open } = useWebSocket('/ws', { immediate: false, onMessage(...) })
onMounted(() => open())
```

Compared to a typical Socket.IO setup — rooms, namespaces, adapters, Redis pub/sub configuration — this is radically simpler. One handler file, one module-level variable, and it worked locally on the first try.

## The Break on Deploy

`pnpm dev` ran perfectly. On Vercel, `wss://gospendl.com/ws` sent the `Upgrade: websocket` header, but `101 Switching Protocols` never came back. Chrome DevTools showed "Provisional headers are shown" with an empty response section. Backend Slack notifications for the crawl job kept arriving fine — the WebSocket broadcast just never reached any user.

My first guess was a cross-instance state problem: the in-memory `peers` Set only exists inside a single serverless instance, so if a user's WebSocket connection landed on instance A and the broadcast fired from instance B, the message would never reach them. That's a real problem for serverless WebSockets in general — but it wasn't what was happening here. The connection wasn't even being established in the first place.

## Root Cause

The Nitro Vercel preset runtime handler, in `nitropack` 2.13.1, is a plain HTTP Node listener:

```js
// node_modules/nitropack/dist/presets/vercel/runtime/vercel.mjs
import { toNodeListener } from "h3";
const handler = toNodeListener(nitroApp.h3App);
const listener = function(req, res) { ... return handler(req, res); };
export default listener;
```

When Vercel Functions forwards the upgrade request, `h3`'s `toNodeListener` never returns a `101` response — there's simply no code in the preset that handles WebSocket upgrades. A `grep -rE "websocket|upgrade" presets/vercel/` in `nitropack` comes back empty.

Setting `experimental.websocket: true` in Nitro activates `crossws` — but `crossws` doesn't have a Vercel adapter wired into the `nitropack` 2.x Vercel preset. Nitro 3 (currently `3.0.260610-beta`) does have WebSocket support on Vercel per their docs — but Nuxt 4 is built on `nitropack` 2.x, not 3.

## The Contrast With Next.js

Vercel does support WebSockets in general, on Fluid Compute, since June 2026. For Next.js, there's an explicit escape hatch:

```ts
// app/api/ws/route.ts
import { experimental_upgradeWebSocket } from '@vercel/functions'

export async function GET() {
  return experimental_upgradeWebSocket((ws) => {
    ws.on('message', (data) => ws.send(data))
  })
}
```

`experimental_upgradeWebSocket()` is a Vercel runtime API that performs the upgrade at the function level. Nitro has no equivalent — the Vercel preset would need to integrate that API, and in v2 it doesn't. Vercel's own docs state that "Nitro's native WebSocket support works on Vercel," which is true, but only once a project is running Nitro 3.

## What I Did Instead

I migrated to Server-Sent Events backed by Upstash Redis pub/sub.

::sse-redis-architecture-diagram
::

The SSE endpoint (`server/api/events.get.ts`) gives every connecting client its own `ioredis` subscriber, subscribed to `crawl:events:${VERCEL_ENV}` — environment-scoped so dev, preview, and prod stay isolated from each other. The crawl webhook publishes via the `@upstash/redis` REST client, which works well here since it's a short-lived request rather than something needing a persistent TCP connection.

On the frontend, the swap was a single line: `useWebSocket` became `useEventSource`, with the message shape unchanged.

Redis is the piece that actually solves the cross-instance problem I originally suspected: a publish from instance A and a subscribe on instance B both go through Redis, so it doesn't matter which serverless instance happens to be handling which request.

One small gotcha in the SSE setup: `res.writeHead()` plus `res.flushHeaders()` alone weren't enough to actually push the response to the client. An initial `res.write(': connected\n\n')` byte was necessary to get the response to flush at all — a quirk of how `h3` 1.15 behaves in Nitro's dev-mode request handling.

## The Takeaway

Nuxt/Nitro's WebSocket API is the nicest I've seen in a full-stack framework. One `defineWebSocketHandler` file, one config flag, done — no setup compromise compared to Socket.IO.

But it's a framework-native abstraction that needs a host-specific adapter underneath it. The Nuxt Vercel adapter, tied to the `nitropack` 2.x preset, doesn't implement the upgrade handshake — this isn't Vercel lacking WebSocket support, it's Nitro's Vercel preset not having caught up yet. Next.js ships an explicit escape hatch for exactly this case via `@vercel/functions`.

On Vercel today, that means Nuxt 4 WebSockets work locally and nowhere else — not because Vercel can't do it, but because the adapter that would make it work doesn't exist yet. For production realtime, the options are Server-Sent Events plus a pub/sub layer like Redis, or deploying somewhere that supports a raw, long-lived Node server — Railway, Fly, Render.

## Sources

- [Vercel WebSockets docs](https://vercel.com/docs/functions/websockets) — states Nitro's native WebSocket support works on Vercel, but links to a Nitro WebSockets starter template built on Nitro 3, not Nuxt 4
- [Nitro WebSocket guide](https://nitro.build/guide/websocket) — Nitro 3 docs, shows `features.websocket: true`
- [Vercel's Nitro docs](https://vercel.com/docs/frameworks/nitro) — mentions Fluid Compute as the default, no WebSocket specifics
- `nitropack` Vercel preset source (v2.13.1) — no WebSocket handling code present
