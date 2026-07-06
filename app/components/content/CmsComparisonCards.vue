<template>
  <div class="diagram my-8">
    <svg
      width="100%"
      viewBox="0 0 680 300"
      role="img"
      xmlns="http://www.w3.org/2000/svg"
    >
      <title>CMS comparison: Strapi, Storyblok, Sanity, Contentful</title>
      <desc>Four headless CMS options compared by best use case, pricing model, and key strength.</desc>

      <!-- Strapi -->
      <rect
        x="40"
        y="40"
        width="140"
        height="220"
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
        x="110"
        y="72"
        text-anchor="middle"
      >Strapi</text>
      <line
        x1="56"
        y1="84"
        x2="164"
        y2="84"
        :stroke="tealStroke"
        stroke-width="0.5"
        opacity="0.4"
      />
      <text
        :fill="tealSub"
        font-family="sans-serif"
        font-size="12"
        x="110"
        y="104"
        text-anchor="middle"
      >Open source</text>
      <text
        :fill="tealSub"
        font-family="sans-serif"
        font-size="12"
        x="110"
        y="120"
        text-anchor="middle"
      >Self-hostable</text>
      <text
        :fill="tealSub"
        font-family="sans-serif"
        font-size="12"
        x="110"
        y="136"
        text-anchor="middle"
      >Free to host</text>
      <line
        x1="56"
        y1="152"
        x2="164"
        y2="152"
        :stroke="tealStroke"
        stroke-width="0.5"
        opacity="0.4"
      />
      <text
        :fill="tealSub"
        font-family="sans-serif"
        font-size="12"
        x="110"
        y="172"
        text-anchor="middle"
      >Best for</text>
      <text
        :fill="tealTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="110"
        y="190"
        text-anchor="middle"
      >full control</text>
      <text
        :fill="tealSub"
        font-family="sans-serif"
        font-size="12"
        x="110"
        y="208"
        text-anchor="middle"
      >dev team owns</text>
      <text
        :fill="tealSub"
        font-family="sans-serif"
        font-size="12"
        x="110"
        y="224"
        text-anchor="middle"
      >infrastructure</text>

      <!-- Storyblok -->
      <rect
        x="200"
        y="40"
        width="140"
        height="220"
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
        y="72"
        text-anchor="middle"
      >Storyblok</text>
      <line
        x1="216"
        y1="84"
        x2="324"
        y2="84"
        :stroke="purpleStroke"
        stroke-width="0.5"
        opacity="0.4"
      />
      <text
        :fill="purpleSub"
        font-family="sans-serif"
        font-size="12"
        x="270"
        y="104"
        text-anchor="middle"
      >Visual editor</text>
      <text
        :fill="purpleSub"
        font-family="sans-serif"
        font-size="12"
        x="270"
        y="120"
        text-anchor="middle"
      >Component-based</text>
      <text
        :fill="purpleSub"
        font-family="sans-serif"
        font-size="12"
        x="270"
        y="136"
        text-anchor="middle"
      >SaaS pricing</text>
      <line
        x1="216"
        y1="152"
        x2="324"
        y2="152"
        :stroke="purpleStroke"
        stroke-width="0.5"
        opacity="0.4"
      />
      <text
        :fill="purpleSub"
        font-family="sans-serif"
        font-size="12"
        x="270"
        y="172"
        text-anchor="middle"
      >Best for</text>
      <text
        :fill="purpleTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="270"
        y="190"
        text-anchor="middle"
      >marketing teams</text>
      <text
        :fill="purpleSub"
        font-family="sans-serif"
        font-size="12"
        x="270"
        y="208"
        text-anchor="middle"
      >editors build pages</text>
      <text
        :fill="purpleSub"
        font-family="sans-serif"
        font-size="12"
        x="270"
        y="224"
        text-anchor="middle"
      >without devs</text>

      <!-- Sanity -->
      <rect
        x="360"
        y="40"
        width="140"
        height="220"
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
        x="430"
        y="72"
        text-anchor="middle"
      >Sanity</text>
      <line
        x1="376"
        y1="84"
        x2="484"
        y2="84"
        :stroke="amberStroke"
        stroke-width="0.5"
        opacity="0.4"
      />
      <text
        :fill="amberSub"
        font-family="sans-serif"
        font-size="12"
        x="430"
        y="104"
        text-anchor="middle"
      >Flexible schema</text>
      <text
        :fill="amberSub"
        font-family="sans-serif"
        font-size="12"
        x="430"
        y="120"
        text-anchor="middle"
      >Real-time collab</text>
      <text
        :fill="amberSub"
        font-family="sans-serif"
        font-size="12"
        x="430"
        y="136"
        text-anchor="middle"
      >Free tier available</text>
      <line
        x1="376"
        y1="152"
        x2="484"
        y2="152"
        :stroke="amberStroke"
        stroke-width="0.5"
        opacity="0.4"
      />
      <text
        :fill="amberSub"
        font-family="sans-serif"
        font-size="12"
        x="430"
        y="172"
        text-anchor="middle"
      >Best for</text>
      <text
        :fill="amberTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="430"
        y="190"
        text-anchor="middle"
      >complex content</text>
      <text
        :fill="amberSub"
        font-family="sans-serif"
        font-size="12"
        x="430"
        y="208"
        text-anchor="middle"
      >custom schemas,</text>
      <text
        :fill="amberSub"
        font-family="sans-serif"
        font-size="12"
        x="430"
        y="224"
        text-anchor="middle"
      >steep learning curve</text>

      <!-- Contentful -->
      <rect
        x="520"
        y="40"
        width="140"
        height="220"
        rx="8"
        :fill="blueFill"
        :stroke="blueStroke"
        stroke-width="0.5"
      />
      <text
        :fill="blueTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="590"
        y="72"
        text-anchor="middle"
      >Contentful</text>
      <line
        x1="536"
        y1="84"
        x2="644"
        y2="84"
        :stroke="blueStroke"
        stroke-width="0.5"
        opacity="0.4"
      />
      <text
        :fill="blueSub"
        font-family="sans-serif"
        font-size="12"
        x="590"
        y="104"
        text-anchor="middle"
      >Enterprise-grade</text>
      <text
        :fill="blueSub"
        font-family="sans-serif"
        font-size="12"
        x="590"
        y="120"
        text-anchor="middle"
      >Well-documented</text>
      <text
        :fill="blueSub"
        font-family="sans-serif"
        font-size="12"
        x="590"
        y="136"
        text-anchor="middle"
      >Scales with you</text>
      <line
        x1="536"
        y1="152"
        x2="644"
        y2="152"
        :stroke="blueStroke"
        stroke-width="0.5"
        opacity="0.4"
      />
      <text
        :fill="blueSub"
        font-family="sans-serif"
        font-size="12"
        x="590"
        y="172"
        text-anchor="middle"
      >Best for</text>
      <text
        :fill="blueTitle"
        font-family="sans-serif"
        font-size="14"
        font-weight="500"
        x="590"
        y="190"
        text-anchor="middle"
      >funded startups</text>
      <text
        :fill="blueSub"
        font-family="sans-serif"
        font-size="12"
        x="590"
        y="208"
        text-anchor="middle"
      >pricing scales up</text>
      <text
        :fill="blueSub"
        font-family="sans-serif"
        font-size="12"
        x="590"
        y="224"
        text-anchor="middle"
      >quickly</text>

      <!-- Bottom hint -->
      <text
        :fill="subtitleColor"
        font-family="sans-serif"
        font-size="12"
        x="340"
        y="278"
        text-anchor="middle"
      >Click a card to learn more</text>
    </svg>
  </div>
</template>

<script setup>
const isDark = typeof window !== 'undefined'
  ? window.matchMedia('(prefers-color-scheme: dark)').matches
  : false

const subtitleColor = isDark ? 'rgba(255,255,255,0.4)' : 'rgba(0,0,0,0.4)'

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

const blueFill = isDark ? '#042C53' : '#E6F1FB'
const blueStroke = isDark ? '#378ADD' : '#378ADD'
const blueTitle = isDark ? '#85B7EB' : '#0C447C'
const blueSub = isDark ? '#378ADD' : '#185FA5'
</script>

<style scoped>
.diagram {
  border-radius: 8px;
  overflow: hidden;
}
</style>
