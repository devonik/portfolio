<template>
  <div class="diagram my-8">
    <svg
      width="100%"
      viewBox="0 0 680 340"
      role="img"
      xmlns="http://www.w3.org/2000/svg"
    >
      <title>Traditional CMS vs Headless CMS architecture</title>
      <desc>Left: traditional CMS couples backend and frontend in one system. Right: headless CMS exposes content via API to multiple frontends.</desc>
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
        :fill="titleColor"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="170"
        y="28"
        text-anchor="middle"
      >Traditional CMS</text>
      <text
        :fill="subtitleColor"
        font-family="sans-serif"
        font-size="12"
        x="170"
        y="46"
        text-anchor="middle"
      >(e.g. WordPress)</text>
      <text
        :fill="titleColor"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="490"
        y="28"
        text-anchor="middle"
      >Headless CMS</text>
      <text
        :fill="subtitleColor"
        font-family="sans-serif"
        font-size="12"
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
        :stroke="borderColor"
        stroke-width="0.5"
        stroke-dasharray="4,4"
      />

      <!-- LEFT: Traditional CMS outer box -->
      <rect
        x="60"
        y="62"
        width="220"
        height="190"
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
        fill="none"
        :stroke="coralStroke"
        stroke-width="0.5"
        opacity="0.6"
      />
      <text
        :fill="coralTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="170"
        y="124"
        text-anchor="middle"
      >Content backend</text>
      <text
        :fill="coralSub"
        font-family="sans-serif"
        font-size="12"
        x="170"
        y="142"
        text-anchor="middle"
      >database, admin panel</text>

      <!-- Coupled line -->
      <line
        x1="170"
        y1="156"
        x2="170"
        y2="168"
        :stroke="coralStroke"
        stroke-width="1.5"
      />
      <text
        :fill="subtitleColor"
        font-family="sans-serif"
        font-size="11"
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
        fill="none"
        :stroke="coralStroke"
        stroke-width="0.5"
        opacity="0.6"
      />
      <text
        :fill="coralTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="170"
        y="192"
        text-anchor="middle"
      >Frontend (themes)</text>
      <text
        :fill="coralSub"
        font-family="sans-serif"
        font-size="12"
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
        :stroke="borderColor"
        stroke-width="1"
        marker-end="url(#arrow-hvt)"
      />
      <rect
        x="100"
        y="282"
        width="140"
        height="36"
        rx="4"
        :fill="grayFill"
        :stroke="grayStroke"
        stroke-width="0.5"
      />
      <text
        :fill="grayTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="170"
        y="305"
        text-anchor="middle"
      >One website only</text>

      <!-- RIGHT: Headless CMS box -->
      <rect
        x="360"
        y="62"
        width="180"
        height="72"
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
        x="450"
        y="88"
        text-anchor="middle"
      >Headless CMS</text>
      <text
        :fill="tealSub"
        font-family="sans-serif"
        font-size="12"
        x="450"
        y="108"
        text-anchor="middle"
      >content + REST/GraphQL API</text>
      <text
        :fill="tealSub"
        font-family="sans-serif"
        font-size="12"
        x="450"
        y="124"
        text-anchor="middle"
      >no frontend</text>

      <!-- API arrow down -->
      <line
        x1="450"
        y1="134"
        x2="450"
        y2="158"
        :stroke="borderColor"
        stroke-width="1"
        marker-end="url(#arrow-hvt)"
      />
      <text
        :fill="subtitleColor"
        font-family="sans-serif"
        font-size="12"
        x="458"
        y="152"
      >API</text>

      <!-- Frontend: Website -->
      <rect
        x="360"
        y="162"
        width="120"
        height="44"
        rx="4"
        :fill="purpleFill"
        :stroke="purpleStroke"
        stroke-width="0.5"
      />
      <text
        :fill="purpleTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="420"
        y="181"
        text-anchor="middle"
      >Website</text>
      <text
        :fill="purpleSub"
        font-family="sans-serif"
        font-size="12"
        x="420"
        y="197"
        text-anchor="middle"
      >Next.js / Nuxt</text>

      <!-- Frontend: Mobile -->
      <rect
        x="500"
        y="162"
        width="120"
        height="44"
        rx="4"
        :fill="purpleFill"
        :stroke="purpleStroke"
        stroke-width="0.5"
      />
      <text
        :fill="purpleTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="560"
        y="181"
        text-anchor="middle"
      >Mobile app</text>
      <text
        :fill="purpleSub"
        font-family="sans-serif"
        font-size="12"
        x="560"
        y="197"
        text-anchor="middle"
      >React Native</text>

      <!-- Frontend: Any channel -->
      <rect
        x="430"
        y="226"
        width="120"
        height="44"
        rx="4"
        :fill="purpleFill"
        :stroke="purpleStroke"
        stroke-width="0.5"
      />
      <text
        :fill="purpleTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="490"
        y="245"
        text-anchor="middle"
      >Any channel</text>
      <text
        :fill="purpleSub"
        font-family="sans-serif"
        font-size="12"
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
        :stroke="borderColor"
        stroke-width="1"
        marker-end="url(#arrow-hvt)"
      />
      <path
        d="M450 160 L560 160 L560 162"
        fill="none"
        :stroke="borderColor"
        stroke-width="1"
        marker-end="url(#arrow-hvt)"
      />
      <path
        d="M450 160 L490 224"
        fill="none"
        :stroke="borderColor"
        stroke-width="1"
        marker-end="url(#arrow-hvt)"
      />

      <!-- Bottom labels -->
      <text
        :fill="subtitleColor"
        font-family="sans-serif"
        font-size="12"
        x="170"
        y="328"
        text-anchor="middle"
      >one output, locked into framework</text>
      <text
        :fill="subtitleColor"
        font-family="sans-serif"
        font-size="12"
        x="490"
        y="308"
        text-anchor="middle"
      >content once → any frontend</text>
    </svg>
  </div>
</template>

<script setup>
const isDark = typeof window !== 'undefined'
  ? window.matchMedia('(prefers-color-scheme: dark)').matches
  : false

const titleColor = isDark ? '#e8f0f8' : '#1a1a1a'
const subtitleColor = isDark ? 'rgba(255,255,255,0.5)' : 'rgba(0,0,0,0.45)'
const borderColor = isDark ? 'rgba(255,255,255,0.3)' : 'rgba(0,0,0,0.3)'

const coralFill = isDark ? '#3d1a0d' : '#FAECE7'
const coralStroke = isDark ? '#D85A30' : '#D85A30'
const coralTitle = isDark ? '#F0997B' : '#712B13'
const coralSub = isDark ? '#D85A30' : '#993C1D'

const tealFill = isDark ? '#04342C' : '#E1F5EE'
const tealStroke = isDark ? '#1D9E75' : '#1D9E75'
const tealTitle = isDark ? '#5DCAA5' : '#085041'
const tealSub = isDark ? '#1D9E75' : '#0F6E56'

const purpleFill = isDark ? '#26215C' : '#EEEDFE'
const purpleStroke = isDark ? '#7F77DD' : '#7F77DD'
const purpleTitle = isDark ? '#AFA9EC' : '#3C3489'
const purpleSub = isDark ? '#7F77DD' : '#534AB7'

const grayFill = isDark ? '#2C2C2A' : '#F1EFE8'
const grayStroke = isDark ? '#888780' : '#888780'
const grayTitle = isDark ? '#D3D1C7' : '#444441'
</script>

<style scoped>
.diagram {
  border-radius: 8px;
  overflow: hidden;
}
</style>
