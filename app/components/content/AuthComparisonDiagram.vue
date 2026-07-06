<template>
  <div class="acd-diagram">
    <svg
      width="100%"
      viewBox="0 0 680 320"
      role="img"
      xmlns="http://www.w3.org/2000/svg"
    >
      <title>Custom auth vs Supabase Auth comparison</title>
      <desc>Left: what you need to build with custom auth. Right: what Supabase gives you out of the box.</desc>

      <rect
        x="40"
        y="20"
        width="280"
        height="44"
        rx="8"
        class="coral-box"
      />
      <text
        class="coral-title header-text"
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
        class="teal-box"
      />
      <text
        class="teal-title header-text"
        x="500"
        y="47"
        text-anchor="middle"
      >Supabase Auth — out of the box</text>

      <rect
        x="40"
        y="80"
        width="280"
        height="28"
        rx="4"
        class="coral-item"
      />
      <text
        class="coral-title"
        x="180"
        y="98"
        text-anchor="middle"
      >Password hashing (bcrypt / argon2)</text>
      <rect
        x="40"
        y="114"
        width="280"
        height="28"
        rx="4"
        class="coral-item"
      />
      <text
        class="coral-title"
        x="180"
        y="132"
        text-anchor="middle"
      >JWT issuance + validation</text>
      <rect
        x="40"
        y="148"
        width="280"
        height="28"
        rx="4"
        class="coral-item"
      />
      <text
        class="coral-title"
        x="180"
        y="166"
        text-anchor="middle"
      >Refresh token rotation + revocation</text>
      <rect
        x="40"
        y="182"
        width="280"
        height="28"
        rx="4"
        class="coral-item"
      />
      <text
        class="coral-title"
        x="180"
        y="200"
        text-anchor="middle"
      >Secure HTTP-only cookie handling</text>
      <rect
        x="40"
        y="216"
        width="280"
        height="28"
        rx="4"
        class="coral-item"
      />
      <text
        class="coral-title"
        x="180"
        y="234"
        text-anchor="middle"
      >Email verification flow</text>
      <rect
        x="40"
        y="250"
        width="280"
        height="28"
        rx="4"
        class="coral-item"
      />
      <text
        class="coral-title"
        x="180"
        y="268"
        text-anchor="middle"
      >Password reset with rate limiting</text>
      <rect
        x="40"
        y="284"
        width="280"
        height="28"
        rx="4"
        class="coral-item"
      />
      <text
        class="coral-title"
        x="180"
        y="302"
        text-anchor="middle"
      >OAuth provider integration</text>

      <rect
        x="360"
        y="80"
        width="280"
        height="28"
        rx="4"
        class="teal-item"
      />
      <text
        class="teal-title"
        x="500"
        y="98"
        text-anchor="middle"
      >Email / password auth</text>
      <rect
        x="360"
        y="114"
        width="280"
        height="28"
        rx="4"
        class="teal-item"
      />
      <text
        class="teal-title"
        x="500"
        y="132"
        text-anchor="middle"
      >Magic link (passwordless)</text>
      <rect
        x="360"
        y="148"
        width="280"
        height="28"
        rx="4"
        class="teal-item"
      />
      <text
        class="teal-title"
        x="500"
        y="166"
        text-anchor="middle"
      >OAuth: Google, GitHub, Apple + more</text>
      <rect
        x="360"
        y="182"
        width="280"
        height="28"
        rx="4"
        class="teal-item"
      />
      <text
        class="teal-title"
        x="500"
        y="200"
        text-anchor="middle"
      >Phone / SMS auth</text>
      <rect
        x="360"
        y="216"
        width="280"
        height="28"
        rx="4"
        class="teal-item"
      />
      <text
        class="teal-title"
        x="500"
        y="234"
        text-anchor="middle"
      >Multi-factor authentication (TOTP)</text>
      <rect
        x="360"
        y="250"
        width="280"
        height="28"
        rx="4"
        class="teal-item"
      />
      <text
        class="teal-title"
        x="500"
        y="268"
        text-anchor="middle"
      >Row Level Security (RLS) integration</text>
      <rect
        x="360"
        y="284"
        width="280"
        height="28"
        rx="4"
        class="teal-item"
      />
      <text
        class="teal-title"
        x="500"
        y="302"
        text-anchor="middle"
      >Full JS / TS SDK with React hooks</text>

      <text
        class="note"
        x="340"
        y="318"
        text-anchor="middle"
      >Each custom auth item = weeks to build, test, and maintain</text>
    </svg>
  </div>
</template>

<script setup></script>

<style scoped>
.acd-diagram { border-radius: 8px; overflow: hidden; }
svg text { font-family: sans-serif; font-size: 12px; }

.header-text { font-size: 13px; font-weight: 500; }
.note { font-size: 12px; fill: light-dark(rgba(0,0,0,0.4), rgba(255,255,255,0.4)); }

.coral-box  { fill: light-dark(#FAECE7, #3d1a0d); stroke: #D85A30; stroke-width: 0.5; }
.coral-item { fill: light-dark(#FDF4F0, #2a1008); stroke: light-dark(rgba(216,90,48,0.3), rgba(216,90,48,0.3)); stroke-width: 0.5; }
.coral-title { fill: light-dark(#712B13, #F0997B); }

.teal-box  { fill: light-dark(#E1F5EE, #04342C); stroke: #1D9E75; stroke-width: 0.5; }
.teal-item { fill: light-dark(#F0FAF6, #052e27); stroke: light-dark(rgba(29,158,117,0.3), rgba(29,158,117,0.3)); stroke-width: 0.5; }
.teal-title { fill: light-dark(#085041, #5DCAA5); }
</style>
