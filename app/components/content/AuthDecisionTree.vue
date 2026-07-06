<template>
  <div class="diagram my-8">
    <svg
      width="100%"
      viewBox="0 0 680 340"
      role="img"
      xmlns="http://www.w3.org/2000/svg"
    >
      <title>Auth decision tree: 3 questions to choose your auth approach</title>
      <desc>Three questions guide the decision: validating or scaling, enterprise SSO needed, using PostgreSQL.</desc>
      <defs>
        <marker
          id="arrow-adt"
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

      <!-- Q1 -->
      <rect
        x="190"
        y="20"
        width="300"
        height="52"
        rx="8"
        :fill="grayFill"
        :stroke="grayStroke"
        stroke-width="0.5"
      />
      <text
        :fill="grayTitle"
        font-family="sans-serif"
        font-size="13"
        font-weight="500"
        x="340"
        y="42"
        text-anchor="middle"
      >Are you validating or scaling?</text>
      <text
        :fill="grayTitle"
        font-family="sans-serif"
        font-size="12"
        x="340"
        y="60"
        text-anchor="middle"
      >still finding product-market fit?</text>

      <!-- Q1 → Supabase (validating) -->
      <line
        x1="340"
        y1="72"
        x2="340"
        y2="96"
        :stroke="arrowColor"
        stroke-width="1"
        marker-end="url(#arrow-adt)"
      />
      <text
        :fill="subtitleColor"
        font-family="sans-serif"
        font-size="11"
        x="348"
        y="88"
      >validating</text>

      <!-- Supabase result -->
      <rect
        x="190"
        y="98"
        width="300"
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
        x="340"
        y="118"
        text-anchor="middle"
      >Use Supabase Auth</text>
      <text
        :fill="tealSub"
        font-family="sans-serif"
        font-size="12"
        x="340"
        y="134"
        text-anchor="middle"
      >ship fast, focus on product</text>

      <!-- Q1 scaling path -->
      <path
        d="M490 46 L580 46 L580 170"
        fill="none"
        :stroke="arrowColor"
        stroke-width="1"
        marker-end="url(#arrow-adt)"
      />
      <text
        :fill="subtitleColor"
        font-family="sans-serif"
        font-size="11"
        x="496"
        y="40"
      >scaling</text>

      <!-- Q2 -->
      <rect
        x="190"
        y="162"
        width="300"
        height="52"
        rx="8"
        :fill="grayFill"
        :stroke="grayStroke"
        stroke-width="0.5"
      />
      <text
        :fill="grayTitle"
        font-family="sans-serif"
        font-size="13"
        font-weight="500"
        x="340"
        y="184"
        text-anchor="middle"
      >Do customers need enterprise SSO?</text>
      <text
        :fill="grayTitle"
        font-family="sans-serif"
        font-size="12"
        x="340"
        y="200"
        text-anchor="middle"
      >SAML, SCIM provisioning?</text>

      <!-- Arrow Q1→Q2 -->
      <line
        x1="340"
        y1="142"
        x2="340"
        y2="162"
        :stroke="arrowColor"
        stroke-width="1"
        marker-end="url(#arrow-adt)"
      />

      <!-- Q2 → Auth0/custom (yes) -->
      <path
        d="M190 188 L100 188 L100 258"
        fill="none"
        :stroke="arrowColor"
        stroke-width="1"
        marker-end="url(#arrow-adt)"
      />
      <text
        :fill="subtitleColor"
        font-family="sans-serif"
        font-size="11"
        x="106"
        y="184"
      >yes</text>

      <rect
        x="40"
        y="260"
        width="170"
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
        x="125"
        y="280"
        text-anchor="middle"
      >Auth0 or custom</text>
      <text
        :fill="coralSub"
        font-family="sans-serif"
        font-size="12"
        x="125"
        y="296"
        text-anchor="middle"
      >enterprise-grade needed</text>

      <!-- Q2 → Q3 (no) -->
      <line
        x1="340"
        y1="214"
        x2="340"
        y2="234"
        :stroke="arrowColor"
        stroke-width="1"
        marker-end="url(#arrow-adt)"
      />
      <text
        :fill="subtitleColor"
        font-family="sans-serif"
        font-size="11"
        x="348"
        y="228"
      >no</text>

      <!-- Q3 -->
      <rect
        x="190"
        y="236"
        width="300"
        height="52"
        rx="8"
        :fill="grayFill"
        :stroke="grayStroke"
        stroke-width="0.5"
      />
      <text
        :fill="grayTitle"
        font-family="sans-serif"
        font-size="13"
        font-weight="500"
        x="340"
        y="258"
        text-anchor="middle"
      >Are you using PostgreSQL?</text>
      <text
        :fill="grayTitle"
        font-family="sans-serif"
        font-size="12"
        x="340"
        y="274"
        text-anchor="middle"
      >Supabase RLS is the payoff</text>

      <!-- Q3 → Supabase (yes) -->
      <line
        x1="340"
        y1="288"
        x2="340"
        y2="308"
        :stroke="arrowColor"
        stroke-width="1"
        marker-end="url(#arrow-adt)"
      />
      <text
        :fill="subtitleColor"
        font-family="sans-serif"
        font-size="11"
        x="348"
        y="303"
      >yes / no</text>

      <rect
        x="190"
        y="310"
        width="300"
        height="24"
        rx="6"
        :fill="tealFill"
        :stroke="tealStroke"
        stroke-width="0.5"
      />
      <text
        :fill="tealTitle"
        font-family="sans-serif"
        font-size="13"
        font-weight="500"
        x="340"
        y="326"
        text-anchor="middle"
      >Supabase Auth — near-automatic choice</text>

      <!-- Scaling path connects to Q2 -->
      <line
        x1="580"
        y1="170"
        x2="490"
        y2="170"
        :stroke="arrowColor"
        stroke-width="1"
        marker-end="url(#arrow-adt)"
      />
    </svg>
  </div>
</template>

<script setup>
const isDark = typeof window !== 'undefined'
  ? window.matchMedia('(prefers-color-scheme: dark)').matches
  : false

const arrowColor = isDark ? 'rgba(255,255,255,0.35)' : 'rgba(0,0,0,0.35)'
const subtitleColor = isDark ? 'rgba(255,255,255,0.45)' : 'rgba(0,0,0,0.4)'

const grayFill = isDark ? '#2C2C2A' : '#F1EFE8'
const grayStroke = isDark ? '#5F5E5A' : '#B4B2A9'
const grayTitle = isDark ? '#D3D1C7' : '#444441'

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
