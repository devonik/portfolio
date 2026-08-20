---
title: "One Maintenance Session on an Agent-Assisted Client Project"
description: 75 commits, 141 tests, and a schema tool that's banned from the project on purpose. What one maintenance pass on a Claude-Code-assisted booking site actually surfaced, once the seams started showing.
date: 2026-08-18
image: /blog/agent-maintenance-session-hero.png
minRead: 7
author:
  name: Niklas Grieger
  avatar:
    src: /profile.jpg
    alt: Niklas Grieger
---

## The project

Kinderleicht is a booking site for family courses - pregnancy, baby, toddler classes - in Hannover, built for a client as an unpaid portfolio project. Next.js 16 App Router, Storyblok for content, Postgres via Drizzle for anything sensitive, Resend for mail, Stripe prepared but not connected yet, Vercel hosting.

Seven weeks in: 75 commits, 20 issues (13 still open), 18 merged PRs, 141 tests across 12 files, 3 SQL migrations applied by hand, one at a time, per environment, on purpose.

The rule that shapes everything else: public content lives in the CMS, personal data lives in Postgres. Bookings carry children's health information, a special category under GDPR Article 9 - which turns out to matter a lot more than it sounds like it should, as you'll see below.

Storyblok wasn't the first choice, for what it's worth - the project started on Sanity and moved over once it became clear the editor mattered more than the content model for someone who isn't a developer. [Full writeup on that migration, including a public-dataset detail I wasn't expecting](https://www.wpescape.dev/blog/sanity-to-storyblok-migration).

## The agent setup

Issues get written for Claude Code with the full context baked into each one - the stack, the rule about what goes in the CMS versus the database, the footguns that keep biting. A cold agent starts working without needing to ask a follow-up question first.

The context itself is split by sensitivity. The instructions the agent needs to write code are committed to the repo. Anything about pricing, business strategy, or legal terms lives in a file that's gitignored - the cloud agent gets what it needs to do the job, and nothing about the business itself.

A scheduled routine runs every night and works through whatever's ready and needs no human input. Each morning, a human reviews the resulting pull request before it lands on a staging branch, which later ships to production through a separate release PR. A label pair acts as the whole state machine: ready for the agent, then done by the agent. Some tickets are marked explicitly as off-limits to the agent entirely, because they need production credentials, real payment details, or an actual conversation with the client.

::agent-branch-flow-diagram
::

## The tool that's banned from this project, on purpose

The database schema lives in two places that are supposed to agree with each other: hand-written SQL migration files, and a schema file that Drizzle (the query library) reads to know what the tables look like.

There's a popular command that keeps those two in sync automatically - point it at your schema file, and it diffs that against the live database, then makes the database match. Convenient, right up until it decides that "make it match" includes deleting anything the schema file doesn't explicitly describe. In this project, that's every index and every CHECK constraint, including this one:

```sql
constraint participants_health_requires_consent
  check (health_details is null or health_consent_at is not null)
```

Read literally, it says: either the health-details field is empty, or the consent timestamp is filled in. That's SQL's roundabout way of writing "if X, then Y" - there's no direct if/then in a CHECK constraint, so you flip it to "not X, or Y" instead. In practice: the moment someone tries to save an allergy note, the database also requires a consent timestamp to go with it. Skip the consent step, and the health note simply can't be saved - the database itself refuses it.

Health data gets special treatment under EU privacy law (GDPR Article 9): storing it requires explicit, documented consent, not a general "I agree to your terms" checkbox buried in a signup form. In practice that means being able to point to a specific record of when and how someone agreed - which is exactly what `health_consent_at` is: a timestamp written the moment a parent actually consents to their child's health details being stored, not assumed from them submitting the form. The constraint just makes sure that timestamp can never be missing when health data is present, instead of relying on every code path that writes to this table to remember the check.

Run the sync command described above, though, and the app keeps working fine afterward - it just quietly stops enforcing that rule.

So the tool isn't installed. The ban is spelled out in the agent's persistent instructions and repeated in every ticket's context block, because an agent working alone at 2am, with no memory of this conversation, would otherwise have a completely reasonable reason to install it: the project clearly needs a way to sync schema and database, and this is the standard way to do it. Reasonable and wrong don't cancel each other out.

## What one maintenance pass actually turns up

No new features this session - just figuring out why a few things looked stuck, closing what was actually finished, and fixing an infrastructure annoyance that had been quietly costing time.

**"Is turning on payments a one-line flag flip, or a real chunk of work?"** Reading the code answered it faster than guessing would have. A feature flag already gates the relevant behavior, and the database schema already has the payment columns, an idempotency table, and the full status flow built out. What was left came to about a day and a half - and two of those hours were for problems that weren't written down anywhere: the payment webhook would get blocked by the basic-auth protection on the staging environment, and the confirmation email currently fires the moment a booking is created rather than after payment actually succeeds, so that trigger has to move.

**A finished piece of work stayed marked as open, for a mundane reason.** GitHub only auto-closes an issue when the fix lands on the production branch, and this fix had merged into staging first, as everything here does. Not a bug, just a two-stage release process doing exactly what it does.

**Database changes never happen automatically**, on purpose - a deploy to production never touches the database by itself. Someone runs each migration by hand, once per environment. Running the test suite mid-session, three tests failed with an error pointing at a table that didn't exist locally. The migration behind it had shipped to production the day before and had simply never been run against the local database. That's the tradeoff of doing migrations by hand, made visible.

**Branch protection - the setting that stops anyone from merging into staging without review - turned out to be unavailable** on a private repository on the plan this project runs on. The fix became a small automated workflow that rebuilds the staging branch right after each production release, timed carefully so it doesn't collide with GitHub's own cleanup of the branch that was just merged.

## Three near-misses

One piece of work got marked finished by the agent while part of what it was supposed to do was still genuinely unfinished - not because of bad code, but because that remaining part depended on information only the client could provide, and the agent had no way to know that from inside the ticket. The lesson isn't "don't trust the agent." It's that reviewing a pull request has to mean checking it against what the ticket actually asked for, not just reading whether the diff looks reasonable.

Separately, the agent ran into a piece of repository configuration nobody had specifically designed for: the staging branch didn't exist at that exact moment, deleted by an earlier merge, and the agent noticed and correctly redirected its own pull request straight to production instead. The adaptation was the right call. What's worth sitting with is that a setting buried in repo configuration was able to change agent behavior in a way that never showed up in any planning conversation.

And a rollback plan that had been written down as real - a saved snapshot of the previous setup, ready if something went wrong - turned out to exist on exactly one laptop and had never actually been pushed anywhere. Found and fixed this session, before anyone needed it and discovered it wasn't there.

## The takeaway

The agent wrote good code all week. The actual work in this maintenance session was somewhere else - in the seams between systems, where a two-stage branch flow, a review process, and a platform's own limits all meet, and where a ticket can look finished without actually being finished.
