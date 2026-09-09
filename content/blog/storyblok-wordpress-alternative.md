---
title: "Storyblok as a WordPress Alternative: One Client Build"
description: A booking site for a family-course studio, built in about two months. What went into Storyblok, what stayed in Postgres, and why the client maintains her own content without calling me.
date: 2026-09-15
image: /blog/storyblok-wordpress-alternative-hero.png
minRead: 7
author:
  name: Niklas Grieger
  avatar:
    src: /profile.jpg
    alt: Niklas Grieger
---

## The brief

Kinderleicht is a studio for family courses in Hannover: pregnancy groups, baby classes, toddler classes. Built for a client. Her old site was a website builder with no real booking. Parents emailed her to ask about free places, she kept the count in her head, and payment happened in cash at the first session.

She wanted three things: online booking, online payment, and a site she could update herself without paying someone every time a course date moved.

The obvious answer is WordPress with a booking plugin. I built it on Next.js and Storyblok instead.

## About two months, start to live

First commit was early July. The site went to production in early September, with booking opening two weeks later, before the first courses on 1 November.

What shipped in that window:

- Course catalogue and detail pages with a live count of free places
- Booking form with all required fields and separate consent checkboxes
- GDPR Article 9 consent for health data, enforced in the database
- Stripe Checkout on the client's own account, with a reserved-then-paid status flow
- A one-off consultation booking that skips payment and capacity
- A read-only participant overview for the owner, behind a login
- Minimum-participant logic, so a course can be cancelled or merged if fewer than six people sign up
- SEO scaffolding: sitemap, robots, JSON-LD for courses and the local business
- Rate limiting and bot protection on the public booking endpoint
- Imprint, privacy policy and terms, all editable in the CMS

Roughly 140 commits, 45 merged pull requests, 270 tests. Most of the code ran through Claude Code on a nightly schedule with a morning review, which I covered in [a separate writeup on the agent workflow](/blog/agent-maintenance-session).

## The split that does the work

One rule shaped the whole architecture: public content goes in the CMS, personal data goes in Postgres.

Storyblok holds courses, sessions, the cancellation policy, and the about page. That is all public, all low-risk, and all owned by the client. She edits a course description or shifts a date in the visual editor, and the change is live after a webhook revalidation.

Bookings and participants never touch Storyblok. A booking record carries a parent's name and address, a child's name and date of birth, and optionally allergies or health notes. A CMS delivery token is read access to the entire space, so there is no per-record access control worth the name, whatever the vendor. That data lives in a Postgres database in the client's own Neon account, reachable only from the server.

This is also why the project moved off Sanity partway through. Sanity's free plan serves datasets publicly by default, and its editor is a form-based back office rather than a visual one. Storyblok refuses an untokened request and puts the real page in an iframe. For someone who is not a developer, clicking the headline you want to change beats filling in a field and then going to look at the result. I wrote up that migration in detail [on the WPEscape blog](https://www.wpescape.dev/blog/sanity-to-storyblok-migration).

## Article 9 as a database constraint

German and EU law treats health data as a special category. Storing a child's allergy note needs its own explicit consent, separate from the general privacy checkbox, and you have to be able to prove that consent was given.

The form collects a dedicated checkbox for it. But a checkbox in a form is a promise the frontend makes. The database makes its own:

```sql
constraint participants_health_requires_consent
check (health_details is null or health_consent_at is not null)
```

Either the health field is empty, or the consent timestamp is filled in. No code path, no admin action, and no future migration can leave a health note sitting in the table without the timestamp that justifies it. Health details also never leave the database by email. The notification to the owner says only that details exist.

## The free-seats number

The client asked for one thing more than any other: every course page has to show how many places are left, and it has to be right.

That number is maximum capacity minus active bookings, and it changes the moment someone books. So it is never cached. It reads from Postgres on every request, inside its own loading boundary so the rest of the page still renders statically. On a small site this costs nothing and removes an entire category of "but the site said two places were free" emails.

## Why this beats WordPress here, and where it doesn't

The case for the headless setup:

- No plugin stack. A WordPress booking site is the CMS plus a booking plugin plus a payment plugin plus a caching plugin, each with its own update cycle and its own attack surface. This site is one codebase.
- The sensitive data is separated by the architecture, not by a naming convention someone has to remember.
- The client maintains her own content and has not asked me to change a word since launch.
- Hosting is a static frontend with a few server routes, not a PHP host that needs tuning.

The honest costs:

- Storyblok validates one field at a time. "Minimum participants must not exceed maximum" is a rule I can enforce in code but not in the CMS, so in the editor it is a sentence in a field description.
- No reverse references. A query that would have been one call in Sanity's GROQ is now two requests.
- The content schema lives in the Storyblok UI unless you deliberately export it. In a repo it would go through review.
- Someone has to maintain the code. It is far less than a plugin stack, but it is not zero, and it is me.

For a simple blog where the owner loves the WordPress editor, none of this is worth it. For a booking site handling children's health data, the separation alone justifies the build.

## What the client owns

I own the structure: the content types, the booking logic, the database schema, the payment flow. She owns everything a visitor reads: every course, every date, every price, her own words about herself. She has not asked me to change a word of it since launch.

That is the case for a headless CMS as a WordPress alternative. The developer defines the shape once, and a non-technical client fills it in for years, with no plugin stack to keep patched.
