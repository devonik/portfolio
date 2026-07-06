<template>
  <div class="diagram my-8">
    <svg
      width="100%"
      viewBox="0 0 680 160"
      role="img"
      xmlns="http://www.w3.org/2000/svg"
    >
      <title>Railway deploy flow in 4 steps</title>
      <desc>Four steps to deploy on Railway: create project, add Docker image service, enter image name, deploy.</desc>
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

      <!-- Step 1 -->
      <rect
        x="40"
        y="30"
        width="120"
        height="80"
        rx="8"
        :fill="grayFill"
        :stroke="grayStroke"
        stroke-width="0.5"
      />
      <text
        :fill="stepNum"
        font-family="sans-serif"
        font-size="11"
        x="100"
        y="52"
        text-anchor="middle"
      >1</text>
      <text
        :fill="grayTitle"
        font-family="sans-serif"
        font-size="13"
        font-weight="500"
        x="100"
        y="74"
        text-anchor="middle"
      >New project</text>
      <text
        :fill="grayTitle"
        font-family="sans-serif"
        font-size="11"
        x="100"
        y="92"
        text-anchor="middle"
      >railway.com</text>

      <line
        x1="160"
        y1="70"
        x2="183"
        y2="70"
        :stroke="arrowColor"
        stroke-width="1"
        marker-end="url(#arrow-rdf)"
      />

      <!-- Step 2 -->
      <rect
        x="185"
        y="30"
        width="120"
        height="80"
        rx="8"
        :fill="purpleFill"
        :stroke="purpleStroke"
        stroke-width="0.5"
      />
      <text
        :fill="stepNum"
        font-family="sans-serif"
        font-size="11"
        x="245"
        y="52"
        text-anchor="middle"
      >2</text>
      <text
        :fill="purpleTitle"
        font-family="sans-serif"
        font-size="13"
        font-weight="500"
        x="245"
        y="70"
        text-anchor="middle"
      >Add service</text>
      <text
        :fill="purpleSub"
        font-family="sans-serif"
        font-size="11"
        x="245"
        y="86"
        text-anchor="middle"
      >Docker Image</text>
      <text
        :fill="purpleSub"
        font-family="sans-serif"
        font-size="11"
        x="245"
        y="100"
        text-anchor="middle"
      >option</text>

      <line
        x1="305"
        y1="70"
        x2="328"
        y2="70"
        :stroke="arrowColor"
        stroke-width="1"
        marker-end="url(#arrow-rdf)"
      />

      <!-- Step 3 -->
      <rect
        x="330"
        y="30"
        width="120"
        height="80"
        rx="8"
        :fill="amberFill"
        :stroke="amberStroke"
        stroke-width="0.5"
      />
      <text
        :fill="stepNum"
        font-family="sans-serif"
        font-size="11"
        x="390"
        y="52"
        text-anchor="middle"
      >3</text>
      <text
        :fill="amberTitle"
        font-family="sans-serif"
        font-size="13"
        font-weight="500"
        x="390"
        y="70"
        text-anchor="middle"
      >Enter image</text>
      <text
        :fill="amberSub"
        font-family="sans-serif"
        font-size="11"
        x="390"
        y="86"
        text-anchor="middle"
      >unclecode/</text>
      <text
        :fill="amberSub"
        font-family="sans-serif"
        font-size="11"
        x="390"
        y="100"
        text-anchor="middle"
      >crawl4ai</text>

      <line
        x1="450"
        y1="70"
        x2="473"
        y2="70"
        :stroke="arrowColor"
        stroke-width="1"
        marker-end="url(#arrow-rdf)"
      />

      <!-- Step 4 -->
      <rect
        x="475"
        y="30"
        width="160"
        height="80"
        rx="8"
        :fill="tealFill"
        :stroke="tealStroke"
        stroke-width="1"
      />
      <text
        :fill="stepNum"
        font-family="sans-serif"
        font-size="11"
        x="555"
        y="52"
        text-anchor="middle"
      >4</text>
      <text
        :fill="tealTitle"
        font-family="sans-serif"
        font-size="13"
        font-weight="500"
        x="555"
        y="70"
        text-anchor="middle"
      >Deploy ✓</text>
      <text
        :fill="tealSub"
        font-family="sans-serif"
        font-size="11"
        x="555"
        y="86"
        text-anchor="middle"
      >live in minutes</text>
      <text
        :fill="tealSub"
        font-family="sans-serif"
        font-size="11"
        x="555"
        y="100"
        text-anchor="middle"
      >8 GB RAM, $5/mo</text>

      <!-- Bottom note -->
      <text
        :fill="subtitleColor"
        font-family="sans-serif"
        font-size="12"
        x="340"
        y="144"
        text-anchor="middle"
      >no railway.json, no Dockerfile, no environment variables needed</text>
    </svg>
  </div>
</template>

<script setup>
const isDark = typeof window !== 'undefined'
  ? window.matchMedia('(prefers-color-scheme: dark)').matches
  : false

const arrowColor = isDark ? 'rgba(255,255,255,0.35)' : 'rgba(0,0,0,0.35)'
const subtitleColor = isDark ? 'rgba(255,255,255,0.4)' : 'rgba(0,0,0,0.4)'
const stepNum = isDark ? 'rgba(255,255,255,0.35)' : 'rgba(0,0,0,0.3)'

const grayFill = isDark ? '#2C2C2A' : '#F1EFE8'
const grayStroke = isDark ? '#5F5E5A' : '#B4B2A9'
const grayTitle = isDark ? '#D3D1C7' : '#444441'

const purpleFill = isDark ? '#26215C' : '#EEEDFE'
const purpleStroke = isDark ? '#7F77DD' : '#7F77DD'
const purpleTitle = isDark ? '#AFA9EC' : '#3C3489'
const purpleSub = isDark ? '#7F77DD' : '#534AB7'

const amberFill = isDark ? '#412402' : '#FAEEDA'
const amberStroke = isDark ? '#BA7517' : '#BA7517'
const amberTitle = isDark ? '#EF9F27' : '#633806'
const amberSub = isDark ? '#BA7517' : '#854F0B'

const tealFill = isDark ? '#04342C' : '#E1F5EE'
const tealStroke = isDark ? '#1D9E75' : '#1D9E75'
const tealTitle = isDark ? '#5DCAA5' : '#085041'
const tealSub = isDark ? '#1D9E75' : '#0F6E56'
</script>

<style scoped>
.diagram { border-radius: 8px; overflow: hidden; }
</style>
