<template>
  <div class="eba-diagram">
    <svg
      width="100%"
      viewBox="0 0 680 240"
      role="img"
      xmlns="http://www.w3.org/2000/svg"
    >
      <title>ESLint setup: before vs after</title>
      <desc>Left: complicated setup with ESLint, Prettier, and VSCode conflicts. Right: simple setup with antfu ESLint config.</desc>
      <defs>
        <marker
          id="arrow-eba"
          viewBox="0 0 10 10"
          refX="8"
          refY="5"
          markerWidth="6"
          markerHeight="6"
          orient="auto-start-reverse"
        >
          <path
            d="M2 1L8 5L2 9"
            fill="none"
            stroke="context-stroke"
            stroke-width="1.5"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </marker>
      </defs>

      <rect
        x="40"
        y="20"
        width="260"
        height="36"
        rx="8"
        class="coral-box"
      />
      <text
        class="coral-title header"
        x="170"
        y="43"
        text-anchor="middle"
      >Before — the mess</text>

      <rect
        x="380"
        y="20"
        width="260"
        height="36"
        rx="8"
        class="teal-box"
      />
      <text
        class="teal-title header"
        x="510"
        y="43"
        text-anchor="middle"
      >After — @antfu/eslint-config</text>

      <rect
        x="40"
        y="72"
        width="260"
        height="28"
        rx="4"
        class="coral-item"
      />
      <text
        class="coral-title"
        x="170"
        y="90"
        text-anchor="middle"
      >ESLint (linting)</text>
      <rect
        x="40"
        y="106"
        width="260"
        height="28"
        rx="4"
        class="coral-item"
      />
      <text
        class="coral-title"
        x="170"
        y="124"
        text-anchor="middle"
      >Prettier (formatting)</text>
      <rect
        x="40"
        y="140"
        width="260"
        height="28"
        rx="4"
        class="coral-item"
      />
      <text
        class="coral-title"
        x="170"
        y="158"
        text-anchor="middle"
      >eslint-prettier plugin (bridge)</text>
      <rect
        x="40"
        y="174"
        width="260"
        height="28"
        rx="4"
        class="coral-item"
      />
      <text
        class="coral-title"
        x="170"
        y="192"
        text-anchor="middle"
      >VSCode formatter conflicts</text>

      <line
        x1="316"
        y1="120"
        x2="368"
        y2="120"
        class="center-arrow"
        marker-end="url(#arrow-eba)"
      />

      <rect
        x="380"
        y="72"
        width="260"
        height="28"
        rx="4"
        class="teal-item"
      />
      <text
        class="teal-title"
        x="510"
        y="90"
        text-anchor="middle"
      >ESLint only (@antfu/eslint-config)</text>
      <rect
        x="380"
        y="106"
        width="260"
        height="28"
        rx="4"
        class="teal-item"
      />
      <text
        class="teal-title"
        x="510"
        y="124"
        text-anchor="middle"
      >Linting + formatting in one</text>
      <rect
        x="380"
        y="140"
        width="260"
        height="28"
        rx="4"
        class="teal-item"
      />
      <text
        class="teal-title"
        x="510"
        y="158"
        text-anchor="middle"
      >VSCode saves = auto-fix</text>
      <rect
        x="380"
        y="174"
        width="260"
        height="28"
        rx="4"
        class="teal-item"
      />
      <text
        class="teal-title"
        x="510"
        y="192"
        text-anchor="middle"
      >Works for TS, Vue, React, JSON...</text>

      <text
        class="note"
        x="340"
        y="228"
        text-anchor="middle"
      >One config, installed in 5 minutes, works for any project size</text>
    </svg>
  </div>
</template>

<script setup></script>

<style scoped>
.eba-diagram { border-radius: 8px; overflow: hidden; }
svg text { font-family: sans-serif; font-size: 12px; }

.header      { font-size: 14px; font-weight: 500; }
.note        { font-size: 12px; fill: light-dark(rgba(0,0,0,0.4), rgba(255,255,255,0.4)); }
.center-arrow { stroke: light-dark(rgba(0,0,0,0.45), rgba(255,255,255,0.55)); stroke-width: 1.5; fill: none; }

.coral-box  { fill: light-dark(#FAECE7, #3d1a0d); stroke: #D85A30; stroke-width: 0.5; }
.coral-item { fill: light-dark(#FDF4F0, #2a1008); stroke: light-dark(rgba(216,90,48,0.3), rgba(216,90,48,0.3)); stroke-width: 0.5; }
.coral-title { fill: light-dark(#712B13, #F0997B); }

.teal-box  { fill: light-dark(#E1F5EE, #04342C); stroke: #1D9E75; stroke-width: 0.5; }
.teal-item { fill: light-dark(#F0FAF6, #052e27); stroke: light-dark(rgba(29,158,117,0.3), rgba(29,158,117,0.3)); stroke-width: 0.5; }
.teal-title { fill: light-dark(#085041, #5DCAA5); }
</style>
