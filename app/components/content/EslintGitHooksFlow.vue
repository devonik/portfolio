<template>
  <div class="egh-diagram">
    <svg
      width="100%"
      viewBox="0 0 680 160"
      role="img"
      xmlns="http://www.w3.org/2000/svg"
    >
      <title>ESLint Git hooks flow</title>
      <desc>git commit triggers pre-commit hook, lint-staged runs ESLint fix, then commit succeeds or fails.</desc>
      <defs>
        <marker
          id="arrow-egh"
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
        y="30"
        width="120"
        height="80"
        rx="8"
        class="gray-box"
      />
      <text
        class="gray-title label"
        x="100"
        y="66"
        text-anchor="middle"
      >git commit</text>
      <text
        class="gray-title sub"
        x="100"
        y="84"
        text-anchor="middle"
      >developer pushes</text>

      <line
        x1="160"
        y1="70"
        x2="183"
        y2="70"
        class="arrow"
        marker-end="url(#arrow-egh)"
      />

      <rect
        x="185"
        y="30"
        width="140"
        height="80"
        rx="8"
        class="purple-box"
      />
      <text
        class="purple-title label"
        x="255"
        y="66"
        text-anchor="middle"
      >pre-commit hook</text>
      <text
        class="purple-sub sub"
        x="255"
        y="84"
        text-anchor="middle"
      >simple-git-hooks fires</text>

      <line
        x1="325"
        y1="70"
        x2="348"
        y2="70"
        class="arrow"
        marker-end="url(#arrow-egh)"
      />

      <rect
        x="350"
        y="30"
        width="140"
        height="80"
        rx="8"
        class="amber-box"
      />
      <text
        class="amber-title label"
        x="420"
        y="58"
        text-anchor="middle"
      >lint-staged</text>
      <text
        class="amber-sub sub"
        x="420"
        y="76"
        text-anchor="middle"
      >ESLint --fix runs</text>
      <text
        class="amber-sub sub"
        x="420"
        y="94"
        text-anchor="middle"
      >on staged files only</text>

      <line
        x1="490"
        y1="70"
        x2="513"
        y2="70"
        class="arrow"
        marker-end="url(#arrow-egh)"
      />

      <rect
        x="515"
        y="20"
        width="140"
        height="44"
        rx="8"
        class="teal-box"
      />
      <text
        class="teal-title label"
        x="585"
        y="40"
        text-anchor="middle"
      >✓ commit ok</text>
      <text
        class="teal-sub sub"
        x="585"
        y="56"
        text-anchor="middle"
      >clean code merged</text>

      <rect
        x="515"
        y="76"
        width="140"
        height="44"
        rx="8"
        class="coral-box"
      />
      <text
        class="coral-title label"
        x="585"
        y="96"
        text-anchor="middle"
      >✗ blocked</text>
      <text
        class="coral-sub sub"
        x="585"
        y="112"
        text-anchor="middle"
      >fix errors first</text>

      <text
        class="note"
        x="340"
        y="148"
        text-anchor="middle"
      >runs only on staged files — fast even in large projects</text>
    </svg>
  </div>
</template>

<script setup></script>

<style scoped>
.egh-diagram { border-radius: 8px; overflow: hidden; }
svg text { font-family: sans-serif; }

.label { font-size: 14px; font-weight: 500; }
.sub   { font-size: 12px; }
.note  { font-size: 12px; fill: light-dark(rgba(0,0,0,0.4), rgba(255,255,255,0.4)); }
.arrow { stroke: light-dark(rgba(0,0,0,0.4), rgba(255,255,255,0.5)); stroke-width: 1; fill: none; }

.gray-box   { fill: light-dark(#F1EFE8, #2C2C2A); stroke: light-dark(#B4B2A9, #5F5E5A); stroke-width: 0.5; }
.gray-title { fill: light-dark(#444441, #D3D1C7); }

.purple-box   { fill: light-dark(#EEEDFE, #26215C); stroke: #7F77DD; stroke-width: 0.5; }
.purple-title { fill: light-dark(#3C3489, #AFA9EC); }
.purple-sub   { fill: light-dark(#534AB7, #7F77DD); }

.amber-box   { fill: light-dark(#FAEEDA, #412402); stroke: #BA7517; stroke-width: 0.5; }
.amber-title { fill: light-dark(#633806, #EF9F27); }
.amber-sub   { fill: light-dark(#854F0B, #BA7517); }

.teal-box  { fill: light-dark(#E1F5EE, #04342C); stroke: #1D9E75; stroke-width: 0.5; }
.teal-title { fill: light-dark(#085041, #5DCAA5); }
.teal-sub   { fill: light-dark(#0F6E56, #1D9E75); }

.coral-box  { fill: light-dark(#FAECE7, #3d1a0d); stroke: #D85A30; stroke-width: 0.5; }
.coral-title { fill: light-dark(#712B13, #F0997B); }
.coral-sub   { fill: light-dark(#993C1D, #D85A30); }
</style>
