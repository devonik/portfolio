<template>
  <div class="rpc-diagram">
    <svg
      width="100%"
      viewBox="0 0 680 200"
      role="img"
      xmlns="http://www.w3.org/2000/svg"
    >
      <title>Hosting cost comparison: Namecheap vs DigitalOcean vs Railway</title>
      <desc>Three options compared by RAM, cost per year, and ops overhead.</desc>

      <rect
        x="40"
        y="20"
        width="180"
        height="160"
        rx="8"
        class="gray-box"
      />
      <text
        class="gray-title card-title"
        x="130"
        y="50"
        text-anchor="middle"
      >Namecheap VPS</text>
      <line
        x1="56"
        y1="60"
        x2="204"
        y2="60"
        class="gray-divider"
      />
      <text
        class="gray-title ram"
        x="130"
        y="82"
        text-anchor="middle"
      >4 GB RAM</text>
      <text
        class="gray-title price"
        x="130"
        y="118"
        text-anchor="middle"
      >$107</text>
      <text
        class="gray-title per-year"
        x="130"
        y="136"
        text-anchor="middle"
      >per year</text>
      <text
        class="gray-title ops"
        x="130"
        y="158"
        text-anchor="middle"
      >manual setup + maintenance</text>

      <rect
        x="250"
        y="20"
        width="180"
        height="160"
        rx="8"
        class="coral-box"
      />
      <text
        class="coral-title card-title"
        x="340"
        y="50"
        text-anchor="middle"
      >DigitalOcean</text>
      <line
        x1="266"
        y1="60"
        x2="414"
        y2="60"
        class="coral-divider"
      />
      <text
        class="coral-title ram"
        x="340"
        y="82"
        text-anchor="middle"
      >4 GB RAM</text>
      <text
        class="coral-title price"
        x="340"
        y="118"
        text-anchor="middle"
      >$288</text>
      <text
        class="coral-title per-year"
        x="340"
        y="136"
        text-anchor="middle"
      >per year</text>
      <text
        class="coral-title ops"
        x="340"
        y="158"
        text-anchor="middle"
      >manual setup + maintenance</text>

      <rect
        x="460"
        y="20"
        width="180"
        height="160"
        rx="8"
        class="teal-box"
      />
      <text
        class="teal-title card-title"
        x="550"
        y="50"
        text-anchor="middle"
      >Railway</text>
      <line
        x1="476"
        y1="60"
        x2="624"
        y2="60"
        class="teal-divider"
      />
      <text
        class="teal-title ram"
        x="550"
        y="82"
        text-anchor="middle"
      >8 GB RAM</text>
      <text
        class="teal-title price"
        x="550"
        y="118"
        text-anchor="middle"
      >$60</text>
      <text
        class="teal-title per-year"
        x="550"
        y="136"
        text-anchor="middle"
      >per year</text>
      <text
        class="teal-title ops"
        x="550"
        y="158"
        text-anchor="middle"
      >zero ops overhead</text>
    </svg>
  </div>
</template>

<script setup></script>

<style scoped>
.rpc-diagram { border-radius: 8px; overflow: hidden; }
svg text { font-family: sans-serif; }

.card-title { font-size: 14px; font-weight: 500; }
.ram        { font-size: 12px; }
.price      { font-size: 28px; font-weight: 500; }
.per-year   { font-size: 12px; }
.ops        { font-size: 12px; }

.gray-box     { fill: light-dark(#F1EFE8, #2C2C2A); stroke: light-dark(#B4B2A9, #5F5E5A); stroke-width: 0.5; }
.gray-title   { fill: light-dark(#444441, #D3D1C7); }
.gray-divider { stroke: light-dark(rgba(136,135,128,0.4), rgba(136,135,128,0.4)); stroke-width: 0.5; }

.coral-box     { fill: light-dark(#FAECE7, #3d1a0d); stroke: #D85A30; stroke-width: 0.5; }
.coral-title   { fill: light-dark(#712B13, #F0997B); }
.coral-divider { stroke: light-dark(rgba(216,90,48,0.4), rgba(216,90,48,0.4)); stroke-width: 0.5; }

.teal-box     { fill: light-dark(#E1F5EE, #04342C); stroke: #1D9E75; stroke-width: 1; }
.teal-title   { fill: light-dark(#085041, #5DCAA5); }
.teal-divider { stroke: light-dark(rgba(29,158,117,0.4), rgba(29,158,117,0.4)); stroke-width: 0.5; }
</style>
