---
title: "Migrating a Live B2B Platform to AWS Without Stopping the Business"
description: A four-year migration moved a veterinary industry webshop off a legacy monolith onto an orchestrated AWS architecture, service by service, without ever pausing the live business.
date: 2026-07-10
image: /blog/migrating-live-b2b-platform-aws-hero.png
minRead: 9
author:
  name: Niklas Grieger
  avatar:
    src: /profile.jpg
    alt: Niklas Grieger
---

For over four years, I led the migration of a B2B platform in the veterinary industry — a monolith that had grown into a small ecosystem of products — onto AWS. No big-bang rewrite, no maintenance window. The business kept running the entire time.

## The Starting Point

The core product was a webshop where veterinary clinics could order supplies — this was the business, the thing that paid the bills. As it grew, the next product built on top of it was a practice management system (PMS): appointment calendars, medical case tracking, vaccination schedules. The calendar feature ended up in daily use by clinics, even though the rest of the PMS was never fully finished. Later still, two more products joined the ecosystem: a supplier portal where suppliers uploaded and edited product data via Excel or a dedicated API, and a B2C booking product — think Doctolib — where clinics could send customers individual links to book appointments with fairly complex scheduling logic.

The monolith holding all of this together had two problems that made it genuinely painful to work with.

The frontend was built on a custom Vue setup with hand-rolled server-side rendering — before Nuxt was mature enough to be the obvious choice. Every component mounted as its own separate Vue app instance. Compiling the project locally took several minutes. Hot reload didn't exist. Every small change meant a coffee break.

The search was running on a legacy AWS Elasticsearch cluster: slow, expensive, and no longer receiving updates. It needed a full rebuild, not a patch.

## Strategy: Strangler Fig, Not Big Bang

With a live business depending on this system, a full rewrite was never on the table. Instead, we migrated one service at a time — pulling functionality out of the monolith into standalone AWS services while the old system kept serving traffic for everything not yet migrated. Over time, the service landscape grew to include a dedicated mail service, a clinic settings API, a rebuilt search service, and more — each one replacing a slice of the monolith without requiring the rest to change at the same time.

## Deep Dive: Rebuilding Search from Scratch

The legacy Elasticsearch cluster wasn't just slow — it was a liability. No updates, rising cost, and a growing product catalog it struggled to keep up with. The rebuild moved everything onto OpenSearch, with new indexing logic built around a single goal: reindexing should never be visible to a user mid-search.

The solution was a Step Functions state machine with a blue/green pattern:

```
Collect → CreateIndex → Insert → UpdateAlias
```

::blue-green-reindex-diagram
::

`Collect` pulls current product data and stages it in S3. `CreateIndex` creates a brand new OpenSearch index — timestamped, so it never collides with the live one — including the synonym mappings that power product search. `Insert` reads the staged data back from S3 and bulk-inserts it in batches. Only once the new index is fully populated does `UpdateAlias` do the actual switch: the search alias gets atomically pointed at the new index, and the old index plus the staging file get cleaned up.

If any step fails, the state machine catches it and routes to a `Failed` state that removes the half-built index and staging file, then posts a Slack alert with a direct link to the failed execution. No user ever sees a half-finished index — either the switch happens cleanly, or nothing changes and the old index keeps serving traffic while someone gets paged.

## Deep Dive: The Frontend Rebuild

This one was my personal highlight of the whole migration — partly because the "before" was so rough.

The old frontend wasn't built on Nuxt or any standard SSR setup. It was a custom, hand-rolled construct: vanilla JavaScript orchestrating server-side rendering, with every single Vue component mounted as its own separate app instance rather than one coherent application tree. There was no framework doing the heavy lifting — just custom glue code trying to reimplement what SSR frameworks already solve.

::frontend-rebuild-diagram
::

The practical cost of that showed up every day. Compiling the project locally took several minutes. Hot reload simply didn't exist — every change meant a full rebuild and a wait. Iterating on a UI detail became a multi-minute round trip instead of an instant feedback loop.

The rebuilt frontends — webshop, PMS, pet-owner portal, supplier admin — were all built on Vue with Nuxt and its standard SSR setup. No custom orchestration layer, no per-component app instances. Just the framework doing what it's designed to do. Local compile times dropped from minutes to seconds, and hot reload just worked. It sounds like a small thing next to state machines and event-driven search, but it changed how the whole team experienced working on the codebase, every single day.

## Orchestration in the PMS

Not everything in this migration was choreographed through events. The PMS backend, built with Spring Boot, took on a different role: it became the central orchestrator, talking synchronously to the newer AWS services via a reactive `WebClient` — mail through the email service, clinic settings through the clinic API, product data through the search service.

::architecture-overview-diagram
::

Two details from that integration layer stood out as worth sharing.

The connection to the search service was contract-first: an OpenAPI spec for the search API was checked into the repo, and the Java client was generated from it at build time. That meant the Java monolith consumed a TypeScript Lambda's API with full type safety — no hand-maintained DTOs slowly drifting out of sync with the actual API.

For tracing across this mix of Elastic Beanstalk apps and Lambda functions, there was no AWS X-Ray or OpenTelemetry in place. Instead, a custom trace ID was generated per request and passed through every `WebClient` call, appearing in every log line across every service it touched. A saved CloudWatch Logs Insights query, filtered on that ID, gave a full cross-service trace on demand. Lightweight, and it worked — a pragmatic answer to a problem usually solved with a managed tracing service.

## Lessons Learned

Not every decision aged perfectly, and a case study that only tells the success story isn't a very useful one.

Despite the PMS using a reactive stack (Spring WebFlux, `WebClient`), `.block()` calls showed up in a few places — for example, when stopping a scheduled email. That defeats the point of going reactive in the first place. It worked, but it's the kind of thing that's easy to introduce under deadline pressure and easy to miss in review, because the code still compiles and runs fine either way.

One Lambda handler in the mail service was written to serve two different callers: a direct HTTP request via API Gateway, and a Step Functions task for scheduled sends. A single flag switched its error behavior between throwing an exception (for Step Functions to catch) and returning an HTTP 500 (for the API caller). It was a pragmatic way to avoid duplicating logic, but in hindsight, one function serving two calling conventions is exactly the kind of thing that gets harder to reason about a year later, when someone new has to figure out why the error handling looks the way it does.

And to be fair about scope: the pieces of the system I can speak to directly used Step Functions catch-and-compensate logic for failure handling, not SQS dead-letter queues or explicit retry policies. That may well have existed elsewhere in parts of the system I didn't touch — but I'd rather be precise about what I actually built than imply a broader pattern than what I can back up.

## Conclusion

Four years, four products, and a business that never had to stop for the migration to happen. The parts I'm proudest of aren't the individually clever pieces — the blue/green reindex, the contract-first API — but that the whole thing held together while staying live: service by service, without a rewrite freeze, without a "migration weekend," without ever asking the business to wait.
