<template>
  <svg viewBox="0 0 920 400" xmlns="http://www.w3.org/2000/svg" class="w-full h-auto" role="img" aria-label="Branch flow: Claude works issues on feature branches into preview, a human reviews the PR, preview ships to main via a release PR, then a GitHub Actions workflow recreates the preview branch">
    <defs>
      <marker id="arrowhead" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" class="fill-primary-400 dark:fill-primary-500" />
      </marker>
    </defs>

    <!-- Claude cloud routine -->
    <g transform="translate(90,80)">
      <rect x="-80" y="-32" width="160" height="64" rx="10" stroke-width="1.5" class="fill-primary-50 dark:fill-primary-950 stroke-primary-300 dark:stroke-primary-700" />
      <text x="0" y="-6" text-anchor="middle" font-size="13" font-weight="700" class="fill-primary-700 dark:fill-primary-300">Claude cloud</text>
      <text x="0" y="12" text-anchor="middle" font-size="11" class="fill-neutral-500 dark:fill-neutral-400">2am, ReadyForClaude</text>
    </g>

    <line x1="170" y1="80" x2="260" y2="80" stroke-width="2" marker-end="url(#arrowhead)" class="stroke-primary-400 dark:stroke-primary-500" />

    <!-- PR into preview -->
    <g transform="translate(340,80)">
      <rect x="-80" y="-32" width="160" height="64" rx="10" stroke-width="1.5" class="fill-neutral-100 dark:fill-neutral-800 stroke-neutral-300 dark:stroke-neutral-600" />
      <text x="0" y="-6" text-anchor="middle" font-size="13" font-weight="700" class="fill-neutral-700 dark:fill-neutral-200">PR opened</text>
      <text x="0" y="12" text-anchor="middle" font-size="11" class="fill-neutral-500 dark:fill-neutral-400">target: preview</text>
    </g>

    <line x1="340" y1="112" x2="340" y2="160" stroke-width="2" marker-end="url(#arrowhead)" class="stroke-neutral-400 dark:stroke-neutral-500" />

    <!-- Human review -->
    <g transform="translate(340,200)">
      <rect x="-90" y="-32" width="180" height="64" rx="10" stroke-width="1.5" class="fill-neutral-100 dark:fill-neutral-800 stroke-neutral-300 dark:stroke-neutral-600" />
      <text x="0" y="-6" text-anchor="middle" font-size="13" font-weight="700" class="fill-neutral-700 dark:fill-neutral-200">Human review</text>
      <text x="0" y="12" text-anchor="middle" font-size="11" class="fill-neutral-500 dark:fill-neutral-400">checks completeness, not just diff</text>
    </g>

    <line x1="430" y1="200" x2="520" y2="200" stroke-width="2" marker-end="url(#arrowhead)" class="stroke-primary-400 dark:stroke-primary-500" />

    <!-- preview branch -->
    <g transform="translate(610,200)">
      <rect x="-90" y="-32" width="180" height="64" rx="10" stroke-width="1.5" class="fill-primary-50 dark:fill-primary-950 stroke-primary-300 dark:stroke-primary-700" />
      <text x="0" y="-6" text-anchor="middle" font-size="13" font-weight="700" class="fill-primary-700 dark:fill-primary-300">preview branch</text>
      <text x="0" y="12" text-anchor="middle" font-size="11" class="fill-neutral-500 dark:fill-neutral-400">no branch protection (free plan)</text>
    </g>

    <line x1="610" y1="232" x2="610" y2="280" stroke-width="2" marker-end="url(#arrowhead)" class="stroke-neutral-400 dark:stroke-neutral-500" />

    <!-- release PR to main -->
    <g transform="translate(610,320)">
      <rect x="-90" y="-32" width="180" height="64" rx="10" stroke-width="1.5" class="fill-neutral-100 dark:fill-neutral-800 stroke-neutral-300 dark:stroke-neutral-600" />
      <text x="0" y="-6" text-anchor="middle" font-size="13" font-weight="700" class="fill-neutral-700 dark:fill-neutral-200">Release PR</text>
      <text x="0" y="12" text-anchor="middle" font-size="11" class="fill-neutral-500 dark:fill-neutral-400">preview → main</text>
    </g>

    <line x1="520" y1="320" x2="440" y2="320" stroke-width="2" marker-end="url(#arrowhead)" class="stroke-neutral-400 dark:stroke-neutral-500" />

    <!-- main -->
    <g transform="translate(340,320)">
      <rect x="-80" y="-32" width="160" height="64" rx="10" stroke-width="1.5" class="fill-primary-50 dark:fill-primary-950 stroke-primary-300 dark:stroke-primary-700" />
      <text x="0" y="-6" text-anchor="middle" font-size="13" font-weight="700" class="fill-primary-700 dark:fill-primary-300">main</text>
      <text x="0" y="12" text-anchor="middle" font-size="11" class="fill-neutral-500 dark:fill-neutral-400">default branch, auto-closes issues</text>
    </g>

    <!-- recreation workflow, dashed loop back to preview -->
    <path d="M 610 288 C 680 315, 705 250, 685 200 C 672 175, 655 168, 640 168" fill="none" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#arrowhead)" class="stroke-neutral-400 dark:stroke-neutral-500" />
    <text x="770" y="245" text-anchor="start" font-size="11" class="fill-neutral-500 dark:fill-neutral-400">GitHub Action</text>
    <text x="770" y="260" text-anchor="start" font-size="11" class="fill-neutral-500 dark:fill-neutral-400">recreates preview</text>
    <text x="770" y="275" text-anchor="start" font-size="11" class="fill-neutral-500 dark:fill-neutral-400">(with wait loop)</text>

    <text x="90" y="30" font-size="12" class="fill-neutral-400 dark:fill-neutral-500">issues in, releases out - preview is the seam</text>
  </svg>
</template>
