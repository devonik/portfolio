<template>
  <div class="diagram my-8">
    <svg
      width="100%"
      viewBox="0 0 680 240"
      role="img"
      xmlns="http://www.w3.org/2000/svg"
    >
      <title>ESLint setup: before vs after</title>
      <desc>Left: the old complicated setup with ESLint plus Prettier plus VSCode formatter conflicts. Right: the simple setup with just antfu ESLint config.</desc>
      <defs>
        <marker
          id="arrow-eb"
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

      <!-- Column headers -->
      <rect
        x="40"
        y="20"
        width="260"
        height="36"
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
        x="170"
        y="43"
        text-anchor="middle"
      >Before — the mess</text>

      <rect
        x="380"
        y="20"
        width="260"
        height="36"
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
        x="510"
        y="43"
        text-anchor="middle"
      >After — @antfu/eslint-config</text>

      <!-- Before items -->
      <g
        v-for="(item, i) in beforeItems"
        :key="'b'+i"
      >
        <rect
          :x="40"
          :y="72 + i * 36"
          width="260"
          height="28"
          rx="4"
          :fill="coralItemFill"
          :stroke="coralStroke"
          stroke-width="0.5"
          opacity="0.8"
        />
        <text
          :fill="coralTitle"
          font-family="sans-serif"
          font-size="12"
          :x="170"
          :y="72 + i * 36 + 18"
          text-anchor="middle"
        >{{ item }}</text>
      </g>

      <!-- Divider arrow -->
      <line
        x1="316"
        y1="120"
        x2="368"
        y2="120"
        :stroke="arrowColor"
        stroke-width="1.5"
        marker-end="url(#arrow-eb)"
      />

      <!-- After items -->
      <g
        v-for="(item, i) in afterItems"
        :key="'a'+i"
      >
        <rect
          :x="380"
          :y="72 + i * 36"
          width="260"
          height="28"
          rx="4"
          :fill="tealItemFill"
          :stroke="tealStroke"
          stroke-width="0.5"
          opacity="0.8"
        />
        <text
          :fill="tealTitle"
          font-family="sans-serif"
          font-size="12"
          :x="510"
          :y="72 + i * 36 + 18"
          text-anchor="middle"
        >{{ item }}</text>
      </g>

      <!-- Bottom note -->
      <text
        :fill="subtitleColor"
        font-family="sans-serif"
        font-size="12"
        x="340"
        y="226"
        text-anchor="middle"
      >One config, installed in 5 minutes, works for any project size</text>
    </svg>
  </div>
</template>

<script setup>
const isDark = typeof window !== 'undefined'
  ? window.matchMedia('(prefers-color-scheme: dark)').matches
  : false

const arrowColor = isDark ? 'rgba(255,255,255,0.5)' : 'rgba(0,0,0,0.4)'
const subtitleColor = isDark ? 'rgba(255,255,255,0.4)' : 'rgba(0,0,0,0.4)'

const coralFill = isDark ? '#3d1a0d' : '#FAECE7'
const coralItemFill = isDark ? '#2a1008' : '#FDF4F0'
const coralStroke = isDark ? '#D85A30' : '#D85A30'
const coralTitle = isDark ? '#F0997B' : '#712B13'

const tealFill = isDark ? '#04342C' : '#E1F5EE'
const tealItemFill = isDark ? '#052e27' : '#F0FAF6'
const tealStroke = isDark ? '#1D9E75' : '#1D9E75'
const tealTitle = isDark ? '#5DCAA5' : '#085041'

const beforeItems = [
  'ESLint (linting)',
  'Prettier (formatting)',
  'eslint-prettier plugin (bridge)',
  'VSCode formatter conflicts'
]

const afterItems = [
  'ESLint only (@antfu/eslint-config)',
  'Linting + formatting in one',
  'VSCode saves = auto-fix',
  'Works for TS, Vue, React, JSON...'
]
</script>

<style scoped>
.diagram { border-radius: 8px; overflow: hidden; }
</style>
