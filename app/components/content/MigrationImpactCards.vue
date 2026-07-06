<template>
  <div class="mic-diagram">
    <svg
      width="100%"
      viewBox="0 0 680 160"
      role="img"
      xmlns="http://www.w3.org/2000/svg"
    >
      <title>Real-world migration impact</title>
      <desc>Four outcomes: 70% faster page loads, 15+ plugins eliminated, reduced hosting costs, improved developer experience.</desc>

      <rect
        x="40"
        y="20"
        width="140"
        height="120"
        rx="8"
        class="teal-box"
      />
      <text
        class="big-num teal-title"
        x="110"
        y="78"
        text-anchor="middle"
      >70%</text>
      <text
        class="teal-sub"
        x="110"
        y="100"
        text-anchor="middle"
      >faster page loads</text>
      <text
        class="teal-sub"
        x="110"
        y="116"
        text-anchor="middle"
      >after migration</text>

      <rect
        x="200"
        y="20"
        width="140"
        height="120"
        rx="8"
        class="purple-box"
      />
      <text
        class="big-num purple-title"
        x="270"
        y="78"
        text-anchor="middle"
      >15+</text>
      <text
        class="purple-sub"
        x="270"
        y="100"
        text-anchor="middle"
      >plugins eliminated</text>
      <text
        class="purple-sub"
        x="270"
        y="116"
        text-anchor="middle"
      >zero maintenance</text>

      <rect
        x="360"
        y="20"
        width="140"
        height="120"
        rx="8"
        class="amber-box"
      />
      <text
        class="big-num amber-title"
        x="430"
        y="78"
        text-anchor="middle"
      >↓</text>
      <text
        class="amber-sub"
        x="430"
        y="100"
        text-anchor="middle"
      >hosting costs</text>
      <text
        class="amber-sub"
        x="430"
        y="116"
        text-anchor="middle"
      >leaner infrastructure</text>

      <rect
        x="520"
        y="20"
        width="140"
        height="120"
        rx="8"
        class="green-box"
      />
      <text
        class="big-num green-title"
        x="590"
        y="78"
        text-anchor="middle"
      >✓</text>
      <text
        class="green-sub"
        x="590"
        y="100"
        text-anchor="middle"
      >better dev experience</text>
      <text
        class="green-sub"
        x="590"
        y="116"
        text-anchor="middle"
      >modern headless stack</text>
    </svg>
  </div>
</template>

<script setup></script>

<style scoped>
.mic-diagram { border-radius: 8px; overflow: hidden; }
svg text { font-family: sans-serif; font-size: 12px; }
.big-num { font-size: 28px; font-weight: 500; }

.teal-box   { fill: light-dark(#E1F5EE, #04342C); stroke: #1D9E75; stroke-width: 0.5; }
.teal-title { fill: light-dark(#085041, #5DCAA5); }
.teal-sub   { fill: light-dark(#0F6E56, #1D9E75); }

.purple-box   { fill: light-dark(#EEEDFE, #26215C); stroke: #7F77DD; stroke-width: 0.5; }
.purple-title { fill: light-dark(#3C3489, #AFA9EC); }
.purple-sub   { fill: light-dark(#534AB7, #7F77DD); }

.amber-box   { fill: light-dark(#FAEEDA, #412402); stroke: #BA7517; stroke-width: 0.5; }
.amber-title { fill: light-dark(#633806, #EF9F27); }
.amber-sub   { fill: light-dark(#854F0B, #BA7517); }

.green-box   { fill: light-dark(#EAF3DE, #173404); stroke: #639922; stroke-width: 0.5; }
.green-title { fill: light-dark(#27500A, #97C459); }
.green-sub   { fill: light-dark(#3B6D11, #639922); }
</style>
