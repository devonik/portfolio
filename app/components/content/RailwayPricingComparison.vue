<template>
  <div class="diagram my-8">
    <svg
      width="100%"
      viewBox="0 0 680 200"
      role="img"
      xmlns="http://www.w3.org/2000/svg"
    >
      <title>Hosting cost comparison: Namecheap vs DigitalOcean vs Railway</title>
      <desc>Three options compared by RAM, cost per year, and ops overhead.</desc>

      <!-- Namecheap -->
      <rect
        x="40"
        y="20"
        width="180"
        height="160"
        rx="8"
        :fill="grayFill"
        :stroke="grayStroke"
        stroke-width="0.5"
      />
      <text
        :fill="grayTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="130"
        y="50"
        text-anchor="middle"
      >Namecheap VPS</text>
      <line
        x1="56"
        y1="60"
        x2="204"
        y2="60"
        :stroke="grayStroke"
        stroke-width="0.5"
        opacity="0.5"
      />
      <text
        :fill="grayTitle"
        font-family="sans-serif"
        font-size="12"
        x="130"
        y="82"
        text-anchor="middle"
      >4 GB RAM</text>
      <text
        :fill="grayTitle"
        font-family="sans-serif"
        font-size="22"
        font-weight="500"
        x="130"
        y="118"
        text-anchor="middle"
      >$107</text>
      <text
        :fill="grayTitle"
        font-family="sans-serif"
        font-size="12"
        x="130"
        y="136"
        text-anchor="middle"
      >per year</text>
      <text
        :fill="grayTitle"
        font-family="sans-serif"
        font-size="12"
        x="130"
        y="158"
        text-anchor="middle"
      >manual setup + maintenance</text>

      <!-- DigitalOcean -->
      <rect
        x="250"
        y="20"
        width="180"
        height="160"
        rx="8"
        :fill="coralFill"
        :stroke="coralStroke"
        stroke-width="0.5"
      />
      <text
        :fill="coralTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="340"
        y="50"
        text-anchor="middle"
      >DigitalOcean</text>
      <line
        x1="266"
        y1="60"
        x2="414"
        y2="60"
        :stroke="coralStroke"
        stroke-width="0.5"
        opacity="0.5"
      />
      <text
        :fill="coralTitle"
        font-family="sans-serif"
        font-size="12"
        x="340"
        y="82"
        text-anchor="middle"
      >4 GB RAM</text>
      <text
        :fill="coralTitle"
        font-family="sans-serif"
        font-size="22"
        font-weight="500"
        x="340"
        y="118"
        text-anchor="middle"
      >$288</text>
      <text
        :fill="coralTitle"
        font-family="sans-serif"
        font-size="12"
        x="340"
        y="136"
        text-anchor="middle"
      >per year</text>
      <text
        :fill="coralTitle"
        font-family="sans-serif"
        font-size="12"
        x="340"
        y="158"
        text-anchor="middle"
      >manual setup + maintenance</text>

      <!-- Railway -->
      <rect
        x="460"
        y="20"
        width="180"
        height="160"
        rx="8"
        :fill="tealFill"
        :stroke="tealStroke"
        stroke-width="1"
      />
      <text
        :fill="tealTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="550"
        y="50"
        text-anchor="middle"
      >Railway</text>
      <line
        x1="476"
        y1="60"
        x2="624"
        y2="60"
        :stroke="tealStroke"
        stroke-width="0.5"
        opacity="0.5"
      />
      <text
        :fill="tealTitle"
        font-family="sans-serif"
        font-size="12"
        x="550"
        y="82"
        text-anchor="middle"
      >8 GB RAM</text>
      <text
        :fill="tealTitle"
        font-family="sans-serif"
        font-size="22"
        font-weight="500"
        x="550"
        y="118"
        text-anchor="middle"
      >$60</text>
      <text
        :fill="tealTitle"
        font-family="sans-serif"
        font-size="12"
        x="550"
        y="136"
        text-anchor="middle"
      >per year</text>
      <text
        :fill="tealTitle"
        font-family="sans-serif"
        font-size="12"
        x="550"
        y="158"
        text-anchor="middle"
      >zero ops overhead</text>
    </svg>
  </div>
</template>

<script setup>
const isDark = typeof window !== 'undefined'
  ? window.matchMedia('(prefers-color-scheme: dark)').matches
  : false

const grayFill = isDark ? '#2C2C2A' : '#F1EFE8'
const grayStroke = isDark ? '#5F5E5A' : '#B4B2A9'
const grayTitle = isDark ? '#D3D1C7' : '#444441'

const coralFill = isDark ? '#3d1a0d' : '#FAECE7'
const coralStroke = isDark ? '#D85A30' : '#D85A30'
const coralTitle = isDark ? '#F0997B' : '#712B13'

const tealFill = isDark ? '#04342C' : '#E1F5EE'
const tealStroke = isDark ? '#1D9E75' : '#1D9E75'
const tealTitle = isDark ? '#5DCAA5' : '#085041'
</script>

<style scoped>
.diagram { border-radius: 8px; overflow: hidden; }
</style>
