<template>
  <div class="diagram my-8">
    <svg
      width="100%"
      viewBox="0 0 680 160"
      role="img"
      xmlns="http://www.w3.org/2000/svg"
    >
      <title>Real-world migration impact</title>
      <desc>Four outcomes: 70% faster page loads, 15+ plugins eliminated, reduced hosting costs, improved developer experience.</desc>

      <!-- Card 1: Speed -->
      <rect
        x="40"
        y="20"
        width="140"
        height="120"
        rx="8"
        :fill="tealFill"
        :stroke="tealStroke"
        stroke-width="0.5"
      />
      <text
        :fill="tealTitle"
        font-family="sans-serif"
        font-size="28"
        font-weight="500"
        x="110"
        y="72"
        text-anchor="middle"
      >70%</text>
      <text
        :fill="tealSub"
        font-family="sans-serif"
        font-size="12"
        x="110"
        y="94"
        text-anchor="middle"
      >faster page loads</text>
      <text
        :fill="tealSub"
        font-family="sans-serif"
        font-size="12"
        x="110"
        y="112"
        text-anchor="middle"
      >after migration</text>

      <!-- Card 2: Plugins -->
      <rect
        x="200"
        y="20"
        width="140"
        height="120"
        rx="8"
        :fill="purpleFill"
        :stroke="purpleStroke"
        stroke-width="0.5"
      />
      <text
        :fill="purpleTitle"
        font-family="sans-serif"
        font-size="28"
        font-weight="500"
        x="270"
        y="72"
        text-anchor="middle"
      >15+</text>
      <text
        :fill="purpleSub"
        font-family="sans-serif"
        font-size="12"
        x="270"
        y="94"
        text-anchor="middle"
      >plugins eliminated</text>
      <text
        :fill="purpleSub"
        font-family="sans-serif"
        font-size="12"
        x="270"
        y="112"
        text-anchor="middle"
      >zero maintenance</text>

      <!-- Card 3: Hosting -->
      <rect
        x="360"
        y="20"
        width="140"
        height="120"
        rx="8"
        :fill="amberFill"
        :stroke="amberStroke"
        stroke-width="0.5"
      />
      <text
        :fill="amberTitle"
        font-family="sans-serif"
        font-size="28"
        font-weight="500"
        x="430"
        y="72"
        text-anchor="middle"
      >↓</text>
      <text
        :fill="amberSub"
        font-family="sans-serif"
        font-size="12"
        x="430"
        y="94"
        text-anchor="middle"
      >hosting costs</text>
      <text
        :fill="amberSub"
        font-family="sans-serif"
        font-size="12"
        x="430"
        y="112"
        text-anchor="middle"
      >leaner infrastructure</text>

      <!-- Card 4: DX -->
      <rect
        x="520"
        y="20"
        width="140"
        height="120"
        rx="8"
        :fill="greenFill"
        :stroke="greenStroke"
        stroke-width="0.5"
      />
      <text
        :fill="greenTitle"
        font-family="sans-serif"
        font-size="28"
        font-weight="500"
        x="590"
        y="72"
        text-anchor="middle"
      >✓</text>
      <text
        :fill="greenSub"
        font-family="sans-serif"
        font-size="12"
        x="590"
        y="94"
        text-anchor="middle"
      >better dev experience</text>
      <text
        :fill="greenSub"
        font-family="sans-serif"
        font-size="12"
        x="590"
        y="112"
        text-anchor="middle"
      >modern headless stack</text>
    </svg>
  </div>
</template>

<script setup>
const isDark = typeof window !== 'undefined'
  ? window.matchMedia('(prefers-color-scheme: dark)').matches
  : false

const tealFill = isDark ? '#04342C' : '#E1F5EE'
const tealStroke = isDark ? '#1D9E75' : '#1D9E75'
const tealTitle = isDark ? '#5DCAA5' : '#085041'
const tealSub = isDark ? '#1D9E75' : '#0F6E56'

const purpleFill = isDark ? '#26215C' : '#EEEDFE'
const purpleStroke = isDark ? '#7F77DD' : '#7F77DD'
const purpleTitle = isDark ? '#AFA9EC' : '#3C3489'
const purpleSub = isDark ? '#7F77DD' : '#534AB7'

const amberFill = isDark ? '#412402' : '#FAEEDA'
const amberStroke = isDark ? '#BA7517' : '#BA7517'
const amberTitle = isDark ? '#EF9F27' : '#633806'
const amberSub = isDark ? '#BA7517' : '#854F0B'

const greenFill = isDark ? '#173404' : '#EAF3DE'
const greenStroke = isDark ? '#639922' : '#639922'
const greenTitle = isDark ? '#97C459' : '#27500A'
const greenSub = isDark ? '#639922' : '#3B6D11'
</script>

<style scoped>
.diagram { border-radius: 8px; overflow: hidden; }
</style>
