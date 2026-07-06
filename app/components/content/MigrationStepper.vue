<template>
  <div class="diagram my-8">
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

      <!-- Step 1 -->
      <rect
        x="40"
        y="40"
        width="130"
        height="100"
        rx="8"
        :fill="tealFill"
        :stroke="tealStroke"
        stroke-width="0.5"
      />
      <text
        :fill="stepNum"
        font-family="sans-serif"
        font-size="12"
        x="105"
        y="66"
        text-anchor="middle"
      >Step 1</text>
      <text
        :fill="tealTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="105"
        y="88"
        text-anchor="middle"
      >Connection</text>
      <text
        :fill="tealTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="105"
        y="106"
        text-anchor="middle"
      >setup</text>
      <text
        :fill="tealSub"
        font-family="sans-serif"
        font-size="12"
        x="105"
        y="126"
        text-anchor="middle"
      >WP URL + credentials</text>

      <!-- Arrow 1→2 -->
      <line
        x1="170"
        y1="90"
        x2="195"
        y2="90"
        :stroke="arrowColor"
        stroke-width="1"
        marker-end="url(#arrow-ms)"
      />

      <!-- Step 2 -->
      <rect
        x="197"
        y="40"
        width="130"
        height="100"
        rx="8"
        :fill="purpleFill"
        :stroke="purpleStroke"
        stroke-width="0.5"
      />
      <text
        :fill="stepNum"
        font-family="sans-serif"
        font-size="12"
        x="262"
        y="66"
        text-anchor="middle"
      >Step 2</text>
      <text
        :fill="purpleTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="262"
        y="88"
        text-anchor="middle"
      >Content</text>
      <text
        :fill="purpleTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="262"
        y="106"
        text-anchor="middle"
      >analysis</text>
      <text
        :fill="purpleSub"
        font-family="sans-serif"
        font-size="12"
        x="262"
        y="126"
        text-anchor="middle"
      >detect all structure</text>

      <!-- Arrow 2→3 -->
      <line
        x1="327"
        y1="90"
        x2="352"
        y2="90"
        :stroke="arrowColor"
        stroke-width="1"
        marker-end="url(#arrow-ms)"
      />

      <!-- Step 3 -->
      <rect
        x="354"
        y="40"
        width="130"
        height="100"
        rx="8"
        :fill="amberFill"
        :stroke="amberStroke"
        stroke-width="0.5"
      />
      <text
        :fill="stepNum"
        font-family="sans-serif"
        font-size="12"
        x="419"
        y="66"
        text-anchor="middle"
      >Step 3</text>
      <text
        :fill="amberTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="419"
        y="88"
        text-anchor="middle"
      >Automated</text>
      <text
        :fill="amberTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="419"
        y="106"
        text-anchor="middle"
      >conversion</text>
      <text
        :fill="amberSub"
        font-family="sans-serif"
        font-size="12"
        x="419"
        y="126"
        text-anchor="middle"
      >content + media + SEO</text>

      <!-- Arrow 3→4 -->
      <line
        x1="484"
        y1="90"
        x2="509"
        y2="90"
        :stroke="arrowColor"
        stroke-width="1"
        marker-end="url(#arrow-ms)"
      />

      <!-- Step 4 -->
      <rect
        x="511"
        y="40"
        width="130"
        height="100"
        rx="8"
        :fill="greenFill"
        :stroke="greenStroke"
        stroke-width="0.5"
      />
      <text
        :fill="stepNum"
        font-family="sans-serif"
        font-size="12"
        x="576"
        y="66"
        text-anchor="middle"
      >Step 4</text>
      <text
        :fill="greenTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="576"
        y="88"
        text-anchor="middle"
      >Review</text>
      <text
        :fill="greenTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="576"
        y="106"
        text-anchor="middle"
      >&amp; publish</text>
      <text
        :fill="greenSub"
        font-family="sans-serif"
        font-size="12"
        x="576"
        y="126"
        text-anchor="middle"
      >verify + go live</text>

      <!-- Timeline label -->
      <text
        :fill="subtitleColor"
        font-family="sans-serif"
        font-size="12"
        x="340"
        y="162"
        text-anchor="middle"
      >1–8 hours depending on site size — mostly automated</text>
    </svg>
  </div>
</template>

<script setup>
const isDark = typeof window !== 'undefined'
  ? window.matchMedia('(prefers-color-scheme: dark)').matches
  : false

const arrowColor = isDark ? 'rgba(255,255,255,0.35)' : 'rgba(0,0,0,0.35)'
const subtitleColor = isDark ? 'rgba(255,255,255,0.4)' : 'rgba(0,0,0,0.4)'
const stepNum = isDark ? 'rgba(255,255,255,0.4)' : 'rgba(0,0,0,0.35)'

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
