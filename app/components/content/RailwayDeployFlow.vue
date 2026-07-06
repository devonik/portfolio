<template>
  <div class="rdf-diagram">
    <svg
      width="100%"
      viewBox="0 0 680 160"
      role="img"
      xmlns="http://www.w3.org/2000/svg"
    >
      <title>Railway deploy flow in 4 steps</title>
      <desc>Four steps: create project, add Docker image service, enter image name, deploy.</desc>
      <defs>
        <marker
          id="arrow-rdf"
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
        class="step-num"
        x="100"
        y="52"
        text-anchor="middle"
      >1</text>
      <text
        class="gray-title label"
        x="100"
        y="74"
        text-anchor="middle"
      >New project</text>
      <text
        class="gray-title sub"
        x="100"
        y="92"
        text-anchor="middle"
      >railway.com</text>

      <line
        x1="160"
        y1="70"
        x2="183"
        y2="70"
        class="arrow"
        marker-end="url(#arrow-rdf)"
      />

      <rect
        x="185"
        y="30"
        width="120"
        height="80"
        rx="8"
        class="purple-box"
      />
      <text
        class="step-num"
        x="245"
        y="52"
        text-anchor="middle"
      >2</text>
      <text
        class="purple-title label"
        x="245"
        y="70"
        text-anchor="middle"
      >Add service</text>
      <text
        class="purple-sub sub"
        x="245"
        y="86"
        text-anchor="middle"
      >Docker Image</text>
      <text
        class="purple-sub sub"
        x="245"
        y="100"
        text-anchor="middle"
      >option</text>

      <line
        x1="305"
        y1="70"
        x2="328"
        y2="70"
        class="arrow"
        marker-end="url(#arrow-rdf)"
      />

      <rect
        x="330"
        y="30"
        width="120"
        height="80"
        rx="8"
        class="amber-box"
      />
      <text
        class="step-num"
        x="390"
        y="52"
        text-anchor="middle"
      >3</text>
      <text
        class="amber-title label"
        x="390"
        y="70"
        text-anchor="middle"
      >Enter image</text>
      <text
        class="amber-sub sub"
        x="390"
        y="86"
        text-anchor="middle"
      >unclecode/</text>
      <text
        class="amber-sub sub"
        x="390"
        y="100"
        text-anchor="middle"
      >crawl4ai</text>

      <line
        x1="450"
        y1="70"
        x2="473"
        y2="70"
        class="arrow"
        marker-end="url(#arrow-rdf)"
      />

      <rect
        x="475"
        y="30"
        width="160"
        height="80"
        rx="8"
        class="teal-box"
      />
      <text
        class="step-num"
        x="555"
        y="52"
        text-anchor="middle"
      >4</text>
      <text
        class="teal-title label"
        x="555"
        y="70"
        text-anchor="middle"
      >Deploy ✓</text>
      <text
        class="teal-sub sub"
        x="555"
        y="86"
        text-anchor="middle"
      >live in minutes</text>
      <text
        class="teal-sub sub"
        x="555"
        y="100"
        text-anchor="middle"
      >8 GB RAM, $5/mo</text>

      <text
        class="note"
        x="340"
        y="144"
        text-anchor="middle"
      >no railway.json, no Dockerfile, no environment variables needed</text>
    </svg>
  </div>
</template>

<script setup></script>

<style scoped>
.rdf-diagram { border-radius: 8px; overflow: hidden; }
svg text { font-family: sans-serif; }

.label    { font-size: 14px; font-weight: 500; }
.sub      { font-size: 12px; }
.step-num { font-size: 11px; fill: light-dark(rgba(0,0,0,0.3), rgba(255,255,255,0.35)); }
.note     { font-size: 12px; fill: light-dark(rgba(0,0,0,0.4), rgba(255,255,255,0.4)); }
.arrow    { stroke: light-dark(rgba(0,0,0,0.4), rgba(255,255,255,0.5)); stroke-width: 1; fill: none; }

.gray-box   { fill: light-dark(#F1EFE8, #2C2C2A); stroke: light-dark(#B4B2A9, #5F5E5A); stroke-width: 0.5; }
.gray-title { fill: light-dark(#444441, #D3D1C7); }

.purple-box   { fill: light-dark(#EEEDFE, #26215C); stroke: #7F77DD; stroke-width: 0.5; }
.purple-title { fill: light-dark(#3C3489, #AFA9EC); }
.purple-sub   { fill: light-dark(#534AB7, #7F77DD); }

.amber-box   { fill: light-dark(#FAEEDA, #412402); stroke: #BA7517; stroke-width: 0.5; }
.amber-title { fill: light-dark(#633806, #EF9F27); }
.amber-sub   { fill: light-dark(#854F0B, #BA7517); }

.teal-box  { fill: light-dark(#E1F5EE, #04342C); stroke: #1D9E75; stroke-width: 1; }
.teal-title { fill: light-dark(#085041, #5DCAA5); }
.teal-sub   { fill: light-dark(#0F6E56, #1D9E75); }
</style>
