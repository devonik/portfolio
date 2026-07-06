<template>
  <div class="ms-diagram">
    <svg
      width="100%"
      viewBox="0 0 680 180"
      role="img"
      xmlns="http://www.w3.org/2000/svg"
    >
      <title>WordPress to Strapi migration steps</title>
      <desc>Four steps: connection setup, content analysis, automated conversion, review and publish.</desc>
      <defs>
        <marker
          id="arrow-ms"
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
        y="40"
        width="130"
        height="100"
        rx="8"
        class="teal-box"
      />
      <text
        class="step-num"
        x="105"
        y="64"
        text-anchor="middle"
      >Step 1</text>
      <text
        class="teal-title"
        x="105"
        y="86"
        text-anchor="middle"
      >Connection</text>
      <text
        class="teal-title"
        x="105"
        y="104"
        text-anchor="middle"
      >setup</text>
      <text
        class="teal-sub"
        x="105"
        y="124"
        text-anchor="middle"
      >WP URL + credentials</text>

      <line
        x1="170"
        y1="90"
        x2="195"
        y2="90"
        class="arrow"
        marker-end="url(#arrow-ms)"
      />

      <rect
        x="197"
        y="40"
        width="130"
        height="100"
        rx="8"
        class="purple-box"
      />
      <text
        class="step-num"
        x="262"
        y="64"
        text-anchor="middle"
      >Step 2</text>
      <text
        class="purple-title"
        x="262"
        y="86"
        text-anchor="middle"
      >Content</text>
      <text
        class="purple-title"
        x="262"
        y="104"
        text-anchor="middle"
      >analysis</text>
      <text
        class="purple-sub"
        x="262"
        y="124"
        text-anchor="middle"
      >detect all structure</text>

      <line
        x1="327"
        y1="90"
        x2="352"
        y2="90"
        class="arrow"
        marker-end="url(#arrow-ms)"
      />

      <rect
        x="354"
        y="40"
        width="130"
        height="100"
        rx="8"
        class="amber-box"
      />
      <text
        class="step-num"
        x="419"
        y="64"
        text-anchor="middle"
      >Step 3</text>
      <text
        class="amber-title"
        x="419"
        y="86"
        text-anchor="middle"
      >Automated</text>
      <text
        class="amber-title"
        x="419"
        y="104"
        text-anchor="middle"
      >conversion</text>
      <text
        class="amber-sub"
        x="419"
        y="124"
        text-anchor="middle"
      >content + media + SEO</text>

      <line
        x1="484"
        y1="90"
        x2="509"
        y2="90"
        class="arrow"
        marker-end="url(#arrow-ms)"
      />

      <rect
        x="511"
        y="40"
        width="130"
        height="100"
        rx="8"
        class="green-box"
      />
      <text
        class="step-num"
        x="576"
        y="64"
        text-anchor="middle"
      >Step 4</text>
      <text
        class="green-title"
        x="576"
        y="86"
        text-anchor="middle"
      >Review</text>
      <text
        class="green-title"
        x="576"
        y="104"
        text-anchor="middle"
      >&amp; publish</text>
      <text
        class="green-sub"
        x="576"
        y="124"
        text-anchor="middle"
      >verify + go live</text>

      <text
        class="note"
        x="340"
        y="162"
        text-anchor="middle"
      >1–8 hours depending on site size — mostly automated</text>
    </svg>
  </div>
</template>

<script setup></script>

<style scoped>
.ms-diagram { border-radius: 8px; overflow: hidden; }
svg text { font-family: sans-serif; font-size: 12px; }

.step-num { fill: light-dark(rgba(0,0,0,0.3), rgba(255,255,255,0.35)); }
.note     { font-size: 12px; fill: light-dark(rgba(0,0,0,0.4), rgba(255,255,255,0.4)); }
.arrow    { stroke: light-dark(rgba(0,0,0,0.4), rgba(255,255,255,0.5)); stroke-width: 1; fill: none; }

.teal-box   { fill: light-dark(#E1F5EE, #04342C); stroke: #1D9E75; stroke-width: 0.5; }
.teal-title { font-size: 14px; font-weight: 500; fill: light-dark(#085041, #5DCAA5); }
.teal-sub   { fill: light-dark(#0F6E56, #1D9E75); }

.purple-box   { fill: light-dark(#EEEDFE, #26215C); stroke: #7F77DD; stroke-width: 0.5; }
.purple-title { font-size: 14px; font-weight: 500; fill: light-dark(#3C3489, #AFA9EC); }
.purple-sub   { fill: light-dark(#534AB7, #7F77DD); }

.amber-box   { fill: light-dark(#FAEEDA, #412402); stroke: #BA7517; stroke-width: 0.5; }
.amber-title { font-size: 14px; font-weight: 500; fill: light-dark(#633806, #EF9F27); }
.amber-sub   { fill: light-dark(#854F0B, #BA7517); }

.green-box   { fill: light-dark(#EAF3DE, #173404); stroke: #639922; stroke-width: 0.5; }
.green-title { font-size: 14px; font-weight: 500; fill: light-dark(#27500A, #97C459); }
.green-sub   { fill: light-dark(#3B6D11, #639922); }
</style>
