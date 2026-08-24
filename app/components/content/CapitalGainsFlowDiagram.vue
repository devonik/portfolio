<template>
  <svg viewBox="0 0 800 380" xmlns="http://www.w3.org/2000/svg" class="w-full h-auto"
       role="img" aria-label="Two brokers feed sale data into an MCP-backed tracker, which returns the combined allowance to the skill before it recommends a sale.">
    <defs>
      <marker id="arrowhead" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6"
              markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" class="fill-neutral-400 dark:fill-neutral-500" />
      </marker>
    </defs>

    <!-- Broker A -->
    <g transform="translate(20,40)">
      <rect width="200" height="70" rx="10" stroke-width="1.5"
            class="fill-neutral-100 dark:fill-neutral-800 stroke-neutral-300 dark:stroke-neutral-600" />
      <text x="100" y="30" text-anchor="middle" font-size="15" font-weight="700"
            class="fill-neutral-700 dark:fill-neutral-200">Interactive Brokers</text>
      <text x="100" y="50" text-anchor="middle" font-size="12"
            class="fill-neutral-500 dark:fill-neutral-400">no withholding</text>
    </g>

    <!-- Broker B -->
    <g transform="translate(20,270)">
      <rect width="200" height="70" rx="10" stroke-width="1.5"
            class="fill-neutral-100 dark:fill-neutral-800 stroke-neutral-300 dark:stroke-neutral-600" />
      <text x="100" y="30" text-anchor="middle" font-size="15" font-weight="700"
            class="fill-neutral-700 dark:fill-neutral-200">Trade Republic</text>
      <text x="100" y="50" text-anchor="middle" font-size="12"
            class="fill-neutral-500 dark:fill-neutral-400">own allowance</text>
    </g>

    <!-- MCP Tracker (highlighted) -->
    <g transform="translate(300,150)">
      <rect width="220" height="90" rx="12" stroke-width="2"
            class="fill-primary-50 dark:fill-primary-950 stroke-primary-300 dark:stroke-primary-700" />
      <text x="110" y="36" text-anchor="middle" font-size="16" font-weight="700"
            class="fill-primary-700 dark:fill-primary-300">MCP Tracker</text>
      <text x="110" y="58" text-anchor="middle" font-size="12"
            class="fill-primary-700 dark:fill-primary-300">get_capital_gains_summary</text>
    </g>

    <!-- Skill -->
    <g transform="translate(600,150)">
      <rect width="180" height="90" rx="12" stroke-width="1.5"
            class="fill-neutral-100 dark:fill-neutral-800 stroke-neutral-300 dark:stroke-neutral-600" />
      <text x="90" y="36" text-anchor="middle" font-size="15" font-weight="700"
            class="fill-neutral-700 dark:fill-neutral-200">Sell skill</text>
      <text x="90" y="58" text-anchor="middle" font-size="12"
            class="fill-neutral-500 dark:fill-neutral-400">picks the position</text>
    </g>

    <!-- Connecting lines -->
    <line x1="220" y1="90" x2="300" y2="185" stroke-width="2" marker-end="url(#arrowhead)"
          class="stroke-neutral-400 dark:stroke-neutral-500" />
    <line x1="220" y1="300" x2="300" y2="215" stroke-width="2" marker-end="url(#arrowhead)"
          class="stroke-neutral-400 dark:stroke-neutral-500" />
    <line x1="520" y1="195" x2="600" y2="195" stroke-width="2.5" marker-end="url(#arrowhead)"
          class="stroke-primary-400 dark:stroke-primary-500" />
    <text x="560" y="180" text-anchor="middle" font-size="11" font-weight="600"
          class="fill-primary-600 dark:fill-primary-400">real allowance</text>
  </svg>
</template>
