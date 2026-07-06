<template>
  <div class="diagram my-8">
    <svg
      width="100%"
      viewBox="0 0 680 320"
      role="img"
      xmlns="http://www.w3.org/2000/svg"
    >
      <title>Custom auth vs Supabase Auth comparison</title>
      <desc>Left column: what you need to build with custom auth. Right column: what Supabase gives you out of the box.</desc>

      <!-- Column headers -->
      <rect
        x="40"
        y="20"
        width="280"
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
        x="180"
        y="47"
        text-anchor="middle"
      >Custom auth — you build all of this</text>

      <rect
        x="360"
        y="20"
        width="280"
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
        x="500"
        y="47"
        text-anchor="middle"
      >Supabase Auth — out of the box</text>

      <!-- Custom auth items -->
      <g
        v-for="(item, i) in customItems"
        :key="'c'+i"
      >
        <rect
          :x="40"
          :y="80 + i * 34"
          width="280"
          height="28"
          rx="4"
          :fill="coralItemFill"
          :stroke="coralStroke"
          stroke-width="0.5"
          opacity="0.7"
        />
        <text
          :fill="coralTitle"
          font-family="sans-serif"
          font-size="12"
          :x="180"
          :y="80 + i * 34 + 18"
          text-anchor="middle"
        >{{ item }}</text>
      </g>

      <!-- Supabase items -->
      <g
        v-for="(item, i) in supabaseItems"
        :key="'s'+i"
      >
        <rect
          :x="360"
          :y="80 + i * 34"
          width="280"
          height="28"
          rx="4"
          :fill="tealItemFill"
          :stroke="tealStroke"
          stroke-width="0.5"
          opacity="0.7"
        />
        <text
          :fill="tealTitle"
          font-family="sans-serif"
          font-size="12"
          :x="500"
          :y="80 + i * 34 + 18"
          text-anchor="middle"
        >{{ item }}</text>
      </g>

      <!-- Bottom note -->
      <text
        :fill="subtitleColor"
        font-family="sans-serif"
        font-size="12"
        x="340"
        y="306"
        text-anchor="middle"
      >Each custom auth item = weeks to build, test, and maintain</text>
    </svg>
  </div>
</template>

<script setup>
const isDark = typeof window !== 'undefined'
  ? window.matchMedia('(prefers-color-scheme: dark)').matches
  : false

const subtitleColor = isDark ? 'rgba(255,255,255,0.4)' : 'rgba(0,0,0,0.4)'

const coralFill = isDark ? '#3d1a0d' : '#FAECE7'
const coralItemFill = isDark ? '#2a1008' : '#FDF4F0'
const coralStroke = isDark ? '#D85A30' : '#D85A30'
const coralTitle = isDark ? '#F0997B' : '#712B13'

const tealFill = isDark ? '#04342C' : '#E1F5EE'
const tealItemFill = isDark ? '#052e27' : '#F0FAF6'
const tealStroke = isDark ? '#1D9E75' : '#1D9E75'
const tealTitle = isDark ? '#5DCAA5' : '#085041'

const customItems = [
  'Password hashing (bcrypt / argon2)',
  'JWT issuance + validation',
  'Refresh token rotation + revocation',
  'Secure HTTP-only cookie handling',
  'Email verification flow',
  'Password reset with rate limiting',
  'OAuth provider integration',
  'Session invalidation across devices'
]

const supabaseItems = [
  'Email / password auth',
  'Magic link (passwordless)',
  'OAuth: Google, GitHub, Apple + more',
  'Phone / SMS auth',
  'Multi-factor authentication (TOTP)',
  'Row Level Security (RLS) integration',
  'Session management across devices',
  'Full JS / TS SDK with React hooks'
]
</script>

<style scoped>
.diagram { border-radius: 8px; overflow: hidden; }
</style>
