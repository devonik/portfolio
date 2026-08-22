---
title: "Vue vs React: What Vapor Mode Actually Changes"
description: I've built every business project on Vue and Nuxt for seven years, and two recent ones in React and Next.js instead. Here's what genuinely felt different for headless CMS frontends, and why Vue just walked away from the virtual DOM entirely.
date: 2026-08-26
image: /blog/vue-vs-react-hero.png
minRead: 6
author:
  name: Niklas Grieger
  avatar:
    src: /profile.jpg
    alt: Niklas Grieger
---

## Why React, after seven years of Vue

Every business project I've built in the last seven years has been Vue or Nuxt. Two recent exceptions broke that streak: WPEscape's demo frontends, and [Kinderleicht](https://kinderleicht-hannover.de/), a client booking site - both in React and Next.js.

The honest reason is two things, not one deep technical argument: I wanted the learning experience myself, and most people evaluating these kinds of projects are more likely to be running React than Vue. Popularity, not architecture, made the decision - and I say that as someone who's still firmly in the Vue camp.

That's really what this post is - not a benchmark or a "which one wins" argument (for real-world apps, neither does, more on that below). Just what actually felt different switching a Vue-shaped brain over to React for real work, and the one architectural change that's making me rethink the default for my next project.

## What Vapor Mode actually changes

This is the part I didn't see coming when I started looking into it, and it's the real reason I'd point someone toward Vue right now if they're starting something new.

Every mainstream framework has run on the same core idea since 2013: keep a lightweight JavaScript copy of the DOM in memory, diff it against the previous version when state changes, and apply only the minimal set of real DOM updates. React popularized it. Vue adopted it. A decade of framework evolution has mostly been about making that diffing faster and more automatic.

Vue 3.6 broke from that entirely. Vapor Mode compiles components directly to imperative DOM operations at build time - no virtual DOM, no diffing step, no runtime reconciliation to speed up because there's nothing left to reconcile. It's opt-in per component, and worth being clear-eyed about: it's still early, not yet the recommended default for every production app, and adoption is meant to be gradual rather than all-at-once.

React's move in the same period was the React Compiler: automatic memoization, removing the need to hand-tune `useMemo` and `useCallback`. Genuinely useful, and it closes a real gap. But it's still optimizing *inside* the virtual DOM model - React still diffs, just more efficiently. Nothing on React's current roadmap removes the virtual DOM the way Vapor Mode does.

::vapor-vs-vdom-diagram
::

Independent benchmark runs (js-framework-benchmark, among others) put Vapor Mode meaningfully ahead of React for typical UI workloads - some published numbers put it in the same tier as Solid.js and Svelte, frameworks that were built compiler-first from day one rather than bolting it on later. I'd treat the exact multiples the way I treat any framework benchmark - directionally informative, not gospel - but the architectural story behind the numbers is real, not marketing.

That's a genuine fork in direction. Vue is testing whether the industry's decade-old assumption - that a virtual DOM is the price of ergonomic reactivity - still needs to be true. React, for now, is making its version of that assumption faster instead of questioning it. One of those is a more interesting bet on where frontend rendering goes next.

## The thing I still don't love: JSX

Vue separates template and logic into distinct blocks in the same file - `<template>` for markup, `<script setup>` for logic. React's JSX puts them in the same expression: markup and JavaScript/TypeScript interleaved directly.

I get why people like it - one language, no context-switching, full type-checking on your markup for free. But I find Vue's separation more readable and more maintainable, especially once a component gets past trivial size. When markup is its own block, you can see the shape of what renders without also parsing the logic that produced it. That's a personal preference, not an objective ranking - plenty of very good developers feel the opposite.

## State management: more similar than the ecosystems suggest

Two comparisons that made the mental model transfer easier than expected:

**Context API is React's provide/inject.** Same problem (pass data down without prop-drilling through every level), same shape of solution, different syntax.

**Pinia is Vue's answer to what React solves with... a lot of different answers.** In Vue, if you need a proper state store, you reach for Pinia. That's not really a decision anymore - it's the default, endorsed by the core team, and there isn't a serious competing option most people reach for instead. In React, the equivalent decision is genuinely open: Zustand, Redux, Jotai, Recoil, plain Context plus `useReducer` - all valid, all with real tradeoffs, and picking one is an actual decision you have to make and justify. Vue's ecosystem converged. React's didn't, not for this.

Neither is objectively better - a single default lowers decision fatigue, more options serve more use cases. But it's a real, practical difference in what starting a new project feels like.

## So which one, for a headless CMS frontend

If I'm picking for myself, on a new project, with no external pressure: Vue. The developer experience was already better for me before Vapor Mode existed, and now the framework is also making a real architectural bet on where rendering is heading, instead of just polishing what's already there.

That's not the full answer for everyone, though, and I'd be overselling it if I pretended otherwise. For real-world CMS-driven sites - fetching from Strapi, Sanity, or Storyblok, rendering content, handling normal amounts of interactivity - both frameworks are fast enough today that raw performance rarely decides the outcome on its own. And if I'm honest about the market reality that actually shaped my own choice for these two projects: more of the people you'll want to reach, hire, or hand a codebase to are on React. That's worth acknowledging even though it's not the technical reason, and even though it's the reason that usually wins.

Certificates.dev has certification tracks for both, if you want to go deeper on either: [Vue](https://certificates.dev/vuejs?friend=DEVNIK) and [React](https://certificates.dev/react?friend=DEVNIK). *Affiliate links - I'm a partner of certificates.dev.*
