<template>
  <div class="hvt-diagram">
    <svg
      width="100%"
      viewBox="0 0 680 340"
      role="img"
      xmlns="http://www.w3.org/2000/svg"
    >
      <title>Traditional CMS vs Headless CMS architecture</title>
      <desc>Left: traditional CMS couples backend and frontend. Right: headless CMS exposes content via API to multiple frontends.</desc>
      <defs>
        <marker
          id="arrow-hvt"
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

      <!-- Column labels -->
      <text
        class="hvt-title"
        x="170"
        y="28"
        text-anchor="middle"
      >Traditional CMS</text>
      <text
        class="hvt-sub"
        x="170"
        y="46"
        text-anchor="middle"
      >(e.g. WordPress)</text>
      <text
        class="hvt-title"
        x="490"
        y="28"
        text-anchor="middle"
      >Headless CMS</text>
      <text
        class="hvt-sub"
        x="490"
        y="46"
        text-anchor="middle"
      >(e.g. Strapi, Sanity)</text>

      <!-- Divider -->
      <line
        x1="340"
        y1="20"
        x2="340"
        y2="320"
        class="hvt-divider"
      />

      <!-- LEFT: Traditional CMS outer box -->
      <rect
        x="60"
        y="62"
        width="220"
        height="190"
        rx="8"
        class="hvt-coral-box"
      />
      <text
        class="hvt-coral-title"
        x="170"
        y="88"
        text-anchor="middle"
      >CMS monolith</text>

      <!-- Inner: backend -->
      <rect
        x="80"
        y="100"
        width="180"
        height="56"
        rx="4"
        class="hvt-coral-inner"
      />
      <text
        class="hvt-coral-title"
        x="170"
        y="124"
        text-anchor="middle"
      >Content backend</text>
      <text
        class="hvt-coral-sub"
        x="170"
        y="142"
        text-anchor="middle"
      >database, admin panel</text>

      <!-- Coupled -->
      <line
        x1="170"
        y1="156"
        x2="170"
        y2="168"
        class="hvt-coupled-line"
      />
      <text
        class="hvt-sub"
        x="178"
        y="164"
      >tightly coupled</text>

      <!-- Inner: frontend -->
      <rect
        x="80"
        y="168"
        width="180"
        height="56"
        rx="4"
        class="hvt-coral-inner"
      />
      <text
        class="hvt-coral-title"
        x="170"
        y="192"
        text-anchor="middle"
      >Frontend (themes)</text>
      <text
        class="hvt-coral-sub"
        x="170"
        y="210"
        text-anchor="middle"
      >PHP templates, plugins</text>

      <!-- Arrow to one output -->
      <line
        x1="170"
        y1="252"
        x2="170"
        y2="280"
        class="hvt-arrow"
        marker-end="url(#arrow-hvt)"
      />
      <rect
        x="100"
        y="282"
        width="140"
        height="36"
        rx="4"
        class="hvt-gray-box"
      />
      <text
        class="hvt-gray-title"
        x="170"
        y="305"
        text-anchor="middle"
      >One website only</text>

      <!-- RIGHT: Headless CMS -->
      <rect
        x="360"
        y="62"
        width="180"
        height="72"
        rx="8"
        class="hvt-teal-box"
      />
      <text
        class="hvt-teal-title"
        x="450"
        y="88"
        text-anchor="middle"
      >Headless CMS</text>
      <text
        class="hvt-teal-sub"
        x="450"
        y="108"
        text-anchor="middle"
      >content + REST/GraphQL API</text>
      <text
        class="hvt-teal-sub"
        x="450"
        y="124"
        text-anchor="middle"
      >no frontend</text>

      <!-- API arrows -->
      <line
        x1="450"
        y1="134"
        x2="450"
        y2="158"
        class="hvt-arrow"
        marker-end="url(#arrow-hvt)"
      />
      <text
        class="hvt-sub"
        x="458"
        y="152"
      >API</text>

      <!-- Frontends -->
      <rect
        x="360"
        y="162"
        width="120"
        height="44"
        rx="4"
        class="hvt-purple-box"
      />
      <text
        class="hvt-purple-title"
        x="420"
        y="181"
        text-anchor="middle"
      >Website</text>
      <text
        class="hvt-purple-sub"
        x="420"
        y="197"
        text-anchor="middle"
      >Next.js / Nuxt</text>

      <rect
        x="500"
        y="162"
        width="120"
        height="44"
        rx="4"
        class="hvt-purple-box"
      />
      <text
        class="hvt-purple-title"
        x="560"
        y="181"
        text-anchor="middle"
      >Mobile app</text>
      <text
        class="hvt-purple-sub"
        x="560"
        y="197"
        text-anchor="middle"
      >React Native</text>

      <rect
        x="430"
        y="226"
        width="120"
        height="44"
        rx="4"
        class="hvt-purple-box"
      />
      <text
        class="hvt-purple-title"
        x="490"
        y="245"
        text-anchor="middle"
      >Any channel</text>
      <text
        class="hvt-purple-sub"
        x="490"
        y="261"
        text-anchor="middle"
      >email, kiosk, app</text>

      <!-- Lines from API to frontends -->
      <line
        x1="420"
        y1="160"
        x2="420"
        y2="162"
        class="hvt-arrow"
        marker-end="url(#arrow-hvt)"
      />
      <path
        d="M450 160 L560 160 L560 162"
        fill="none"
        class="hvt-arrow"
        marker-end="url(#arrow-hvt)"
      />
      <path
        d="M450 160 L490 224"
        fill="none"
        class="hvt-arrow"
        marker-end="url(#arrow-hvt)"
      />

      <!-- Bottom labels -->
      <text
        class="hvt-sub"
        x="170"
        y="328"
        text-anchor="middle"
      >one output, locked into framework</text>
      <text
        class="hvt-sub"
        x="490"
        y="308"
        text-anchor="middle"
      >content once → any frontend</text>
    </svg>
  </div>
</template>

<script setup></script>

<style scoped>
.hvt-diagram { border-radius: 8px; overflow: hidden; }

svg text { font-family: sans-serif; }

.hvt-title { font-size: 14px; font-weight: 500; fill: light-dark(#1a1a1a, #e8f0f8); }
.hvt-sub   { font-size: 12px; fill: light-dark(rgba(0,0,0,0.45), rgba(255,255,255,0.5)); }

.hvt-divider     { stroke: light-dark(rgba(0,0,0,0.2), rgba(255,255,255,0.2)); stroke-width: 0.5; stroke-dasharray: 4,4; }
.hvt-arrow       { stroke: light-dark(rgba(0,0,0,0.4), rgba(255,255,255,0.5)); stroke-width: 1; fill: none; }
.hvt-coupled-line { stroke: light-dark(#D85A30, #D85A30); stroke-width: 1.5; }

/* Coral (Traditional CMS) */
.hvt-coral-box   { fill: light-dark(#FAECE7, #3d1a0d); stroke: #D85A30; stroke-width: 0.5; }
.hvt-coral-inner { fill: none; stroke: light-dark(rgba(216,90,48,0.4), rgba(216,90,48,0.4)); stroke-width: 0.5; }
.hvt-coral-title { font-size: 14px; font-weight: 500; fill: light-dark(#712B13, #F0997B); }
.hvt-coral-sub   { font-size: 12px; fill: light-dark(#993C1D, #D85A30); }

/* Teal (Headless CMS) */
.hvt-teal-box   { fill: light-dark(#E1F5EE, #04342C); stroke: #1D9E75; stroke-width: 0.5; }
.hvt-teal-title { font-size: 14px; font-weight: 500; fill: light-dark(#085041, #5DCAA5); }
.hvt-teal-sub   { font-size: 12px; fill: light-dark(#0F6E56, #1D9E75); }

/* Purple (frontends) */
.hvt-purple-box   { fill: light-dark(#EEEDFE, #26215C); stroke: #7F77DD; stroke-width: 0.5; }
.hvt-purple-title { font-size: 14px; font-weight: 500; fill: light-dark(#3C3489, #AFA9EC); }
.hvt-purple-sub   { font-size: 12px; fill: light-dark(#534AB7, #7F77DD); }

/* Gray (one website) */
.hvt-gray-box   { fill: light-dark(#F1EFE8, #2C2C2A); stroke: #888780; stroke-width: 0.5; }
.hvt-gray-title { font-size: 14px; font-weight: 500; fill: light-dark(#444441, #D3D1C7); }
</style>
