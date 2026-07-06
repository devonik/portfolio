<template>
  <div class="diagram my-8">
    <svg
      width="100%"
      viewBox="0 0 680 160"
      role="img"
      xmlns="http://www.w3.org/2000/svg"
    >
      <title>ESLint Git hooks flow</title>
      <desc>Code change triggers pre-commit hook, lint-staged runs ESLint fix, then commit succeeds or fails with errors.</desc>
      <defs>
        <marker
          id="arrow-gh"
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

      <!-- Step 1: git commit -->
      <rect
        x="40"
        y="40"
        width="130"
        height="60"
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
        x="105"
        y="66"
        text-anchor="middle"
      >git commit</text>
      <text
        :fill="grayTitle"
        font-family="sans-serif"
        font-size="12"
        x="105"
        y="84"
        text-anchor="middle"
      >developer pushes</text>

      <line
        x1="170"
        y1="70"
        x2="198"
        y2="70"
        :stroke="arrowColor"
        stroke-width="1"
        marker-end="url(#arrow-gh)"
      />

      <!-- Step 2: pre-commit hook -->
      <rect
        x="200"
        y="40"
        width="140"
        height="60"
        rx="8"
        :fill="purpleFill"
        :stroke="purpleStroke"
        stroke-width="0.5"
      />
      <text
        :fill="purpleTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="270"
        y="66"
        text-anchor="middle"
      >pre-commit hook</text>
      <text
        :fill="purpleSub"
        font-family="sans-serif"
        font-size="12"
        x="270"
        y="84"
        text-anchor="middle"
      >simple-git-hooks fires</text>

      <line
        x1="340"
        y1="70"
        x2="368"
        y2="70"
        :stroke="arrowColor"
        stroke-width="1"
        marker-end="url(#arrow-gh)"
      />

      <!-- Step 3: lint-staged -->
      <rect
        x="370"
        y="40"
        width="140"
        height="60"
        rx="8"
        :fill="amberFill"
        :stroke="amberStroke"
        stroke-width="0.5"
      />
      <text
        :fill="amberTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="440"
        y="62"
        text-anchor="middle"
      >lint-staged</text>
      <text
        :fill="amberSub"
        font-family="sans-serif"
        font-size="12"
        x="440"
        y="78"
        text-anchor="middle"
      >ESLint --fix runs</text>
      <text
        :fill="amberSub"
        font-family="sans-serif"
        font-size="12"
        x="440"
        y="94"
        text-anchor="middle"
      >on staged files only</text>

      <!-- Arrow to outcomes -->
      <line
        x1="510"
        y1="70"
        x2="538"
        y2="70"
        :stroke="arrowColor"
        stroke-width="1"
        marker-end="url(#arrow-gh)"
      />

      <!-- Success -->
      <rect
        x="540"
        y="20"
        width="120"
        height="44"
        rx="8"
        :fill="tealFill"
        :stroke="tealStroke"
        stroke-width="0.5"
      />
      <text
        :fill="tealTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="600"
        y="40"
        text-anchor="middle"
      >✓ commit ok</text>
      <text
        :fill="tealSub"
        font-family="sans-serif"
        font-size="12"
        x="600"
        y="56"
        text-anchor="middle"
      >clean code merged</text>

      <!-- Fail -->
      <rect
        x="540"
        y="76"
        width="120"
        height="44"
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
        x="600"
        y="96"
        text-anchor="middle"
      >✗ blocked</text>
      <text
        :fill="coralSub"
        font-family="sans-serif"
        font-size="12"
        x="600"
        y="112"
        text-anchor="middle"
      >fix errors first</text>

      <!-- Bottom note -->
      <text
        :fill="subtitleColor"
        font-family="sans-serif"
        font-size="12"
        x="340"
        y="146"
        text-anchor="middle"
      >runs only on staged files — fast even in large projects</text>
    </svg>
  </div>
</template>

<script setup>
const isDark = typeof window !== 'undefined'
  ? window.matchMedia('(prefers-color-scheme: dark)').matches
  : false

const arrowColor = isDark ? 'rgba(255,255,255,0.35)' : 'rgba(0,0,0,0.35)'
const subtitleColor = isDark ? 'rgba(255,255,255,0.4)' : 'rgba(0,0,0,0.4)'

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

const coralFill = isDark ? '#3d1a0d' : '#FAECE7'
const coralStroke = isDark ? '#D85A30' : '#D85A30'
const coralTitle = isDark ? '#F0997B' : '#712B13'
const coralSub = isDark ? '#D85A30' : '#993C1D'
</script>

<style scoped>
.diagram { border-radius: 8px; overflow: hidden; }
</style>
