<template>
  <div class="adt-diagram">
    <svg
      width="100%"
      viewBox="0 0 680 340"
      role="img"
      xmlns="http://www.w3.org/2000/svg"
    >
      <title>Auth decision tree</title>
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
        class="gray-box"
      />
      <text
        class="gray-title q-text"
        x="340"
        y="42"
        text-anchor="middle"
      >Are you validating or scaling?</text>
      <text
        class="gray-title sub-text"
        x="340"
        y="60"
        text-anchor="middle"
      >still finding product-market fit?</text>

      <line
        x1="340"
        y1="72"
        x2="340"
        y2="96"
        class="arrow"
        marker-end="url(#arrow-adt)"
      />
      <text
        class="branch-label"
        x="348"
        y="88"
      >validating</text>

      <!-- Supabase result 1 -->
      <rect
        x="190"
        y="98"
        width="300"
        height="44"
        rx="8"
        class="teal-box"
      />
      <text
        class="teal-title q-text"
        x="340"
        y="118"
        text-anchor="middle"
      >Use Supabase Auth</text>
      <text
        class="teal-sub sub-text"
        x="340"
        y="134"
        text-anchor="middle"
      >ship fast, focus on product</text>

      <!-- Scaling path -->
      <path
        d="M490 46 L580 46 L580 170"
        fill="none"
        class="arrow"
        marker-end="url(#arrow-adt)"
      />
      <text
        class="branch-label"
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
        class="gray-box"
      />
      <text
        class="gray-title q-text"
        x="340"
        y="184"
        text-anchor="middle"
      >Do customers need enterprise SSO?</text>
      <text
        class="gray-title sub-text"
        x="340"
        y="200"
        text-anchor="middle"
      >SAML, SCIM provisioning?</text>

      <line
        x1="340"
        y1="142"
        x2="340"
        y2="162"
        class="arrow"
        marker-end="url(#arrow-adt)"
      />

      <!-- Yes → Auth0 -->
      <path
        d="M190 188 L100 188 L100 258"
        fill="none"
        class="arrow"
        marker-end="url(#arrow-adt)"
      />
      <text
        class="branch-label"
        x="106"
        y="184"
      >yes</text>
      <rect
        x="40"
        y="260"
        width="170"
        height="44"
        rx="8"
        class="coral-box"
      />
      <text
        class="coral-title q-text"
        x="125"
        y="280"
        text-anchor="middle"
      >Auth0 or custom</text>
      <text
        class="coral-sub sub-text"
        x="125"
        y="296"
        text-anchor="middle"
      >enterprise-grade needed</text>

      <!-- No → Q3 -->
      <line
        x1="340"
        y1="214"
        x2="340"
        y2="234"
        class="arrow"
        marker-end="url(#arrow-adt)"
      />
      <text
        class="branch-label"
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
        class="gray-box"
      />
      <text
        class="gray-title q-text"
        x="340"
        y="258"
        text-anchor="middle"
      >Are you using PostgreSQL?</text>
      <text
        class="gray-title sub-text"
        x="340"
        y="274"
        text-anchor="middle"
      >Supabase RLS is the payoff</text>

      <line
        x1="340"
        y1="288"
        x2="340"
        y2="308"
        class="arrow"
        marker-end="url(#arrow-adt)"
      />
      <text
        class="branch-label"
        x="348"
        y="303"
      >yes / no</text>

      <rect
        x="190"
        y="310"
        width="300"
        height="24"
        rx="6"
        class="teal-box"
      />
      <text
        class="teal-title"
        style="font-size:13px;font-weight:500"
        x="340"
        y="326"
        text-anchor="middle"
      >Supabase Auth — near-automatic choice</text>

      <!-- Scaling connects to Q2 -->
      <line
        x1="580"
        y1="170"
        x2="490"
        y2="170"
        class="arrow"
        marker-end="url(#arrow-adt)"
      />
    </svg>
  </div>
</template>

<script setup></script>

<style scoped>
.adt-diagram { border-radius: 8px; overflow: hidden; }
svg text { font-family: sans-serif; font-size: 12px; }

.q-text      { font-size: 13px; font-weight: 500; }
.sub-text    { font-size: 12px; }
.branch-label { font-size: 11px; fill: light-dark(rgba(0,0,0,0.45), rgba(255,255,255,0.45)); }
.arrow       { stroke: light-dark(rgba(0,0,0,0.4), rgba(255,255,255,0.5)); stroke-width: 1; fill: none; }

.gray-box   { fill: light-dark(#F1EFE8, #2C2C2A); stroke: light-dark(#B4B2A9, #5F5E5A); stroke-width: 0.5; }
.gray-title { fill: light-dark(#444441, #D3D1C7); }

.teal-box { fill: light-dark(#E1F5EE, #04342C); stroke: #1D9E75; stroke-width: 0.5; }
.teal-title { fill: light-dark(#085041, #5DCAA5); }
.teal-sub   { fill: light-dark(#0F6E56, #1D9E75); }

.coral-box { fill: light-dark(#FAECE7, #3d1a0d); stroke: #D85A30; stroke-width: 0.5; }
.coral-title { fill: light-dark(#712B13, #F0997B); }
.coral-sub   { fill: light-dark(#993C1D, #D85A30); }
</style>
