<template>
  <svg viewBox="0 0 800 380" xmlns="http://www.w3.org/2000/svg" class="w-full h-auto" role="img" aria-label="GoSpendl system overview: user search connects to Algolia, fed by a Crawl4AI crawler across shops, with Nostr-based Satsback auth for rewards, hosted on Railway and Vercel">
    <defs>
      <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" class="fill-primary-400 dark:fill-primary-500" />
      </marker>
    </defs>

    <!-- User -->
    <g transform="translate(60,190)">
      <circle r="34" stroke-width="1.5" class="fill-neutral-100 dark:fill-neutral-800 stroke-neutral-300 dark:stroke-neutral-600" />
      <text x="0" y="6" text-anchor="middle" font-size="13" font-weight="600" class="fill-neutral-700 dark:fill-neutral-200">User</text>
    </g>

    <!-- arrow user -> search -->
    <line x1="96" y1="190" x2="210" y2="190" stroke-width="2" marker-end="url(#arrow)" class="stroke-primary-400 dark:stroke-primary-500" />

    <!-- Search / Algolia -->
    <g transform="translate(280,190)">
      <rect x="-70" y="-30" width="140" height="60" rx="10" stroke-width="1.5" class="fill-primary-50 dark:fill-primary-950 stroke-primary-300 dark:stroke-primary-700" />
      <text x="0" y="-4" text-anchor="middle" font-size="13" font-weight="700" class="fill-primary-700 dark:fill-primary-300">Search</text>
      <text x="0" y="14" text-anchor="middle" font-size="11" class="fill-neutral-500 dark:fill-neutral-400">Algolia index</text>
    </g>

    <!-- arrow search -> crawler (down) -->
    <line x1="280" y1="220" x2="280" y2="270" stroke-width="2" marker-end="url(#arrow)" class="stroke-primary-400 dark:stroke-primary-500" />

    <!-- Crawler -->
    <g transform="translate(280,320)">
      <rect x="-90" y="-28" width="180" height="56" rx="10" stroke-width="1.5" class="fill-neutral-100 dark:fill-neutral-800 stroke-neutral-300 dark:stroke-neutral-600" />
      <text x="0" y="-4" text-anchor="middle" font-size="13" font-weight="700" class="fill-neutral-700 dark:fill-neutral-200">Crawl4AI crawler</text>
      <text x="0" y="14" text-anchor="middle" font-size="11" class="fill-neutral-500 dark:fill-neutral-400">CSS-schema extraction</text>
    </g>

    <!-- arrow crawler -> shops -->
    <line x1="370" y1="320" x2="470" y2="320" stroke-width="2" marker-end="url(#arrow)" class="stroke-neutral-400 dark:stroke-neutral-500" />

    <!-- shops -->
    <g transform="translate(540,320)">
      <rect x="-60" y="-28" width="120" height="56" rx="10" stroke-width="1.5" stroke-dasharray="4 3" class="fill-neutral-50 dark:fill-neutral-900 stroke-neutral-300 dark:stroke-neutral-600" />
      <text x="0" y="-4" text-anchor="middle" font-size="13" font-weight="700" class="fill-neutral-600 dark:fill-neutral-300">Shops</text>
      <text x="0" y="14" text-anchor="middle" font-size="11" class="fill-neutral-500 dark:fill-neutral-400">listing pages</text>
    </g>

    <!-- arrow search -> satsback (up) -->
    <line x1="350" y1="175" x2="470" y2="130" stroke-width="2" marker-end="url(#arrow)" class="stroke-primary-400 dark:stroke-primary-500" />

    <!-- Satsback / Nostr -->
    <g transform="translate(560,110)">
      <rect x="-90" y="-30" width="180" height="60" rx="10" stroke-width="1.5" class="fill-primary-50 dark:fill-primary-950 stroke-primary-300 dark:stroke-primary-700" />
      <text x="0" y="-4" text-anchor="middle" font-size="13" font-weight="700" class="fill-primary-700 dark:fill-primary-300">Satsback rewards</text>
      <text x="0" y="14" text-anchor="middle" font-size="11" class="fill-neutral-500 dark:fill-neutral-400">auth via Nostr signEvent</text>
    </g>

    <!-- arrow crawler/search -> hosting -->
    <line x1="340" y1="190" x2="470" y2="230" stroke-width="2" marker-end="url(#arrow)" class="stroke-neutral-400 dark:stroke-neutral-500" />

    <!-- Hosting -->
    <g transform="translate(560,240)">
      <rect x="-90" y="-30" width="180" height="60" rx="10" stroke-width="1.5" class="fill-neutral-100 dark:fill-neutral-800 stroke-neutral-300 dark:stroke-neutral-600" />
      <text x="0" y="-4" text-anchor="middle" font-size="13" font-weight="700" class="fill-neutral-700 dark:fill-neutral-200">Hosting</text>
      <text x="0" y="14" text-anchor="middle" font-size="11" class="fill-neutral-500 dark:fill-neutral-400">Vercel (app) + Railway (crawler)</text>
    </g>

    <!-- legend -->
    <text x="60" y="30" font-size="12" class="fill-neutral-400 dark:fill-neutral-500">one search across every shop, satsback rate included</text>
  </svg>
</template>
