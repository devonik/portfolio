---
title: "Building GoSpendl: A Bitcoin Product Search Engine, End to End"
description: A product search platform for the Bitcoin community, built solo - the crawler that scales without burning LLM tokens, the realtime layer that broke on Vercel, the $5/month host that runs it all. Here's the whole build, and where it stands now.
date: 2026-08-06
image: /blog/gospendl-builder-story-hero.png
minRead: 7
author:
  name: Niklas Grieger
  avatar:
    src: /profile.jpg
    alt: Niklas Grieger
---

## Where the idea came from

A friend of mine uses Satsback regularly - a rewards platform that pays out a bit of Bitcoin (sats) back on purchases made through its partner shops. His complaint was always the same: you have to already know which partner shop you want, go there first, and search from inside it. There's no way to just search "iPhone" and see it across every participating shop at once, let alone compare prices between them.

That's the whole idea behind [GoSpendl](https://gospendl.com): search once, see which shops have it, what the satsback rate is at each one, and compare prices - instead of checking shops one at a time.

I built it solo, end to end - frontend, crawling infrastructure, search, hosting. This post is the build story: what I built, what broke, and what I'd do differently.

## The hard part isn't the search box

The obvious version of this product is easy: a Nuxt frontend, an Algolia index, done. The actual hard part is upstream of that - getting accurate, current product data out of hundreds of shops that all look completely different, without it costing a fortune or falling over the moment a shop redesigns its page.

That single problem shaped almost every technical decision in this project.

::gospendl-architecture-overview
::

## Crawling without burning the token budget

My first instinct was to point an LLM at each shop's page and let it figure out the product data. That works fine for one or two shops. It does not work for hundreds, triggered live on every user search - it turns into a token cost problem fast.

What I landed on was a two-phase approach: use an LLM once per shop, offline, to generate a reusable CSS extraction schema. Every real crawl after that is pure CSS extraction against the stored schema - zero LLM calls, zero token cost, per request. [I wrote up the full details separately](/blog/how-i-built-a-token-efficient-crawler), including the failure modes that cost me the most time - feeding an LLM cleaned HTML instead of raw HTML silently breaks pattern recognition, and an LLM without an explicit "give up if you can't find a pattern" instruction will confidently hallucinate CSS selectors that match nothing.

On a sample of 30 shops, about a third produced a working schema on the first attempt, and the plausibility checks I built in caught most of what would otherwise have been bad data reaching search.

## Realtime, and the adapter that didn't exist yet

The other piece I wanted was realtime: when a crawl job finds new results for something you're searching, you should see it without refreshing. Nuxt 4's native WebSocket API looked perfect for this - minimal setup, worked flawlessly locally.

Deployed to Vercel, it just didn't connect. Turned out this wasn't a Vercel limitation at all - [the gap was one layer down](/blog/nuxt-websockets-vs-vercel), in Nitro's Vercel preset, which doesn't yet implement the WebSocket upgrade handshake that Nuxt 4 depends on. I ended up rebuilding that layer on Server-Sent Events over Redis pub/sub instead, which turned out to solve a second problem for free - it doesn't care which serverless instance is handling which request, unlike the in-memory WebSocket approach I'd started with.

## Self-hosting the crawler for $5 a month

Crawl4AI, the crawler I use, needs a real Chromium browser under the hood - at least 4GB of RAM just to run. My existing VPS had exactly 4GB, total, for everything. [Railway ended up being the answer](/blog/railway-smart-docker-host): point it at a Docker image, no server config, no SSH, and the Hobby plan gives 8GB RAM for $5/month - a fraction of what a comparable VPS upgrade or a DigitalOcean droplet would have cost, with none of the ongoing maintenance.

## Login without a login form

The satsback rewards themselves come through a partnership with Satsback, who gave GoSpendl API access to their partner-shop network. Their side of a purchase is straightforward: go to a partner shop through their browser extension or a redirect link, buy something, and a percentage comes back in sats to your Satsback account.

The interesting part was authentication. There's no email/password, no OAuth - it's entirely Nostr-based. If you have a Nostr browser extension (nos2x, Alby), GoSpendl asks it to sign a small event, sends that signed event to Satsback, and gets back a token for your session. No account creation, nothing to remember - if you already have a Nostr identity, that's your login.

It only fires the first time you actually click a satsback-enabled product, not on every page load, so most people browsing and comparing prices never trigger it at all.

## Where it stands

The crawler works. The realtime layer works. The search works. Technically, this is the part of the project I'm proudest of - it's a genuinely solid piece of infrastructure, and I learned more building the crawling and realtime layers than on most client projects I've billed for.

GoSpendl itself is on pause right now while I figure out what's next for it. The code is live and open source if you want to look under the hood: [github.com/devonik/go-spendl](https://github.com/devonik/go-spendl).
