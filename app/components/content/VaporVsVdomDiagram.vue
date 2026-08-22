<template>
  <svg viewBox="0 0 900 460" xmlns="http://www.w3.org/2000/svg" class="w-full h-auto" role="img" aria-label="Step by step comparison: React's virtual DOM diffing pipeline runs five steps on every update, Vue's Vapor Mode compiles directly to DOM operations at build time with three steps at runtime">
    <defs>
      <marker id="arrowhead" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" class="fill-neutral-400 dark:fill-neutral-500" />
      </marker>
    </defs>

    <text x="20" y="30" font-size="13" font-weight="700" class="fill-neutral-500 dark:fill-neutral-400">REACT · VIRTUAL DOM (every update, at runtime)</text>

    <g transform="translate(20,55)">
      <rect width="150" height="50" rx="8" stroke-width="1.5" class="fill-neutral-100 dark:fill-neutral-800 stroke-neutral-300 dark:stroke-neutral-600" />
      <text x="75" y="30" text-anchor="middle" font-size="13" font-weight="600" class="fill-neutral-700 dark:fill-neutral-200">State changes</text>
    </g>
    <line x1="170" y1="80" x2="200" y2="80" stroke-width="2" marker-end="url(#arrowhead)" class="stroke-neutral-400 dark:stroke-neutral-500" />

    <g transform="translate(200,55)">
      <rect width="150" height="50" rx="8" stroke-width="1.5" class="fill-neutral-100 dark:fill-neutral-800 stroke-neutral-300 dark:stroke-neutral-600" />
      <text x="75" y="30" text-anchor="middle" font-size="13" font-weight="600" class="fill-neutral-700 dark:fill-neutral-200">Re-render</text>
    </g>
    <line x1="350" y1="80" x2="380" y2="80" stroke-width="2" marker-end="url(#arrowhead)" class="stroke-neutral-400 dark:stroke-neutral-500" />

    <g transform="translate(380,55)">
      <rect width="150" height="50" rx="8" stroke-width="1.5" class="fill-neutral-100 dark:fill-neutral-800 stroke-neutral-300 dark:stroke-neutral-600" />
      <text x="75" y="24" text-anchor="middle" font-size="13" font-weight="600" class="fill-neutral-700 dark:fill-neutral-200">Build new</text>
      <text x="75" y="40" text-anchor="middle" font-size="13" font-weight="600" class="fill-neutral-700 dark:fill-neutral-200">virtual tree</text>
    </g>
    <line x1="530" y1="80" x2="560" y2="80" stroke-width="2" marker-end="url(#arrowhead)" class="stroke-neutral-400 dark:stroke-neutral-500" />

    <g transform="translate(560,55)">
      <rect width="150" height="50" rx="8" stroke-width="1.5" class="fill-neutral-100 dark:fill-neutral-800 stroke-neutral-300 dark:stroke-neutral-600" />
      <text x="75" y="24" text-anchor="middle" font-size="13" font-weight="600" class="fill-neutral-700 dark:fill-neutral-200">Diff against</text>
      <text x="75" y="40" text-anchor="middle" font-size="13" font-weight="600" class="fill-neutral-700 dark:fill-neutral-200">previous tree</text>
    </g>
    <line x1="710" y1="80" x2="740" y2="80" stroke-width="2" marker-end="url(#arrowhead)" class="stroke-neutral-400 dark:stroke-neutral-500" />

    <g transform="translate(740,55)">
      <rect width="140" height="50" rx="8" stroke-width="1.5" class="fill-neutral-100 dark:fill-neutral-800 stroke-neutral-300 dark:stroke-neutral-600" />
      <text x="70" y="30" text-anchor="middle" font-size="13" font-weight="600" class="fill-neutral-700 dark:fill-neutral-200">Patch real DOM</text>
    </g>

    <text x="740" y="130" font-size="11" class="fill-neutral-500 dark:fill-neutral-400">repeats in full on the next</text>
    <text x="740" y="145" font-size="11" class="fill-neutral-500 dark:fill-neutral-400">state change, every time</text>

    <line x1="20" y1="190" x2="880" y2="190" stroke-width="1" class="stroke-neutral-300 dark:stroke-neutral-700" />

    <text x="20" y="225" font-size="13" font-weight="700" class="fill-primary-600 dark:fill-primary-400">VUE 3.6 · VAPOR MODE (compiled once, at build time)</text>

    <g transform="translate(20,250)">
      <rect width="150" height="50" rx="8" stroke-width="1.5" class="fill-primary-50 dark:fill-primary-950 stroke-primary-300 dark:stroke-primary-700" />
      <text x="75" y="30" text-anchor="middle" font-size="13" font-weight="600" class="fill-primary-700 dark:fill-primary-300">Template compiled</text>
    </g>
    <line x1="170" y1="275" x2="200" y2="275" stroke-width="2" marker-end="url(#arrowhead)" class="stroke-neutral-400 dark:stroke-neutral-500" />

    <g transform="translate(200,250)">
      <rect width="150" height="50" rx="8" stroke-width="1.5" class="fill-primary-50 dark:fill-primary-950 stroke-primary-300 dark:stroke-primary-700" />
      <text x="75" y="24" text-anchor="middle" font-size="13" font-weight="600" class="fill-primary-700 dark:fill-primary-300">direct DOM</text>
      <text x="75" y="40" text-anchor="middle" font-size="13" font-weight="600" class="fill-primary-700 dark:fill-primary-300">update instructions</text>
    </g>

    <text x="200" y="325" font-size="11" class="fill-neutral-500 dark:fill-neutral-400">no tree, no diff - the compiler already</text>
    <text x="200" y="340" font-size="11" class="fill-neutral-500 dark:fill-neutral-400">knows exactly what changes and where</text>

    <line x1="370" y1="275" x2="400" y2="275" stroke-width="2" marker-end="url(#arrowhead)" class="stroke-primary-400 dark:stroke-primary-500" />

    <g transform="translate(400,250)">
      <rect width="150" height="50" rx="8" stroke-width="1.5" class="fill-primary-50 dark:fill-primary-950 stroke-primary-300 dark:stroke-primary-700" />
      <text x="75" y="30" text-anchor="middle" font-size="13" font-weight="600" class="fill-primary-700 dark:fill-primary-300">Real DOM updated</text>
    </g>

    <text x="20" y="420" font-size="12" class="fill-neutral-400 dark:fill-neutral-500">React: 5 steps, every update. Vapor: 3 steps, and one of them only runs once.</text>
  </svg>
</template>
