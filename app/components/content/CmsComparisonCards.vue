<template>
  <div class="cms-diagram">
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
        class="teal-box"
      />
      <text
        class="teal-title"
        x="110"
        y="72"
        text-anchor="middle"
      >Strapi</text>
      <line
        x1="56"
        y1="84"
        x2="164"
        y2="84"
        class="divider"
      />
      <text
        class="teal-sub"
        x="110"
        y="104"
        text-anchor="middle"
      >Open source</text>
      <text
        class="teal-sub"
        x="110"
        y="120"
        text-anchor="middle"
      >Self-hostable</text>
      <text
        class="teal-sub"
        x="110"
        y="136"
        text-anchor="middle"
      >Free to host</text>
      <line
        x1="56"
        y1="152"
        x2="164"
        y2="152"
        class="divider"
      />
      <text
        class="teal-sub"
        x="110"
        y="172"
        text-anchor="middle"
      >Best for</text>
      <text
        class="teal-title"
        x="110"
        y="190"
        text-anchor="middle"
      >full control</text>
      <text
        class="teal-sub"
        x="110"
        y="208"
        text-anchor="middle"
      >dev team owns</text>
      <text
        class="teal-sub"
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
        class="purple-box"
      />
      <text
        class="purple-title"
        x="270"
        y="72"
        text-anchor="middle"
      >Storyblok</text>
      <line
        x1="216"
        y1="84"
        x2="324"
        y2="84"
        class="divider-purple"
      />
      <text
        class="purple-sub"
        x="270"
        y="104"
        text-anchor="middle"
      >Visual editor</text>
      <text
        class="purple-sub"
        x="270"
        y="120"
        text-anchor="middle"
      >Component-based</text>
      <text
        class="purple-sub"
        x="270"
        y="136"
        text-anchor="middle"
      >SaaS pricing</text>
      <line
        x1="216"
        y1="152"
        x2="324"
        y2="152"
        class="divider-purple"
      />
      <text
        class="purple-sub"
        x="270"
        y="172"
        text-anchor="middle"
      >Best for</text>
      <text
        class="purple-title"
        x="270"
        y="190"
        text-anchor="middle"
      >marketing teams</text>
      <text
        class="purple-sub"
        x="270"
        y="208"
        text-anchor="middle"
      >editors build pages</text>
      <text
        class="purple-sub"
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
        class="amber-box"
      />
      <text
        class="amber-title"
        x="430"
        y="72"
        text-anchor="middle"
      >Sanity</text>
      <line
        x1="376"
        y1="84"
        x2="484"
        y2="84"
        class="divider-amber"
      />
      <text
        class="amber-sub"
        x="430"
        y="104"
        text-anchor="middle"
      >Flexible schema</text>
      <text
        class="amber-sub"
        x="430"
        y="120"
        text-anchor="middle"
      >Real-time collab</text>
      <text
        class="amber-sub"
        x="430"
        y="136"
        text-anchor="middle"
      >Free tier available</text>
      <line
        x1="376"
        y1="152"
        x2="484"
        y2="152"
        class="divider-amber"
      />
      <text
        class="amber-sub"
        x="430"
        y="172"
        text-anchor="middle"
      >Best for</text>
      <text
        class="amber-title"
        x="430"
        y="190"
        text-anchor="middle"
      >complex content</text>
      <text
        class="amber-sub"
        x="430"
        y="208"
        text-anchor="middle"
      >custom schemas,</text>
      <text
        class="amber-sub"
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
        class="blue-box"
      />
      <text
        class="blue-title"
        x="590"
        y="72"
        text-anchor="middle"
      >Contentful</text>
      <line
        x1="536"
        y1="84"
        x2="644"
        y2="84"
        class="divider-blue"
      />
      <text
        class="blue-sub"
        x="590"
        y="104"
        text-anchor="middle"
      >Enterprise-grade</text>
      <text
        class="blue-sub"
        x="590"
        y="120"
        text-anchor="middle"
      >Well-documented</text>
      <text
        class="blue-sub"
        x="590"
        y="136"
        text-anchor="middle"
      >Scales with you</text>
      <line
        x1="536"
        y1="152"
        x2="644"
        y2="152"
        class="divider-blue"
      />
      <text
        class="blue-sub"
        x="590"
        y="172"
        text-anchor="middle"
      >Best for</text>
      <text
        class="blue-title"
        x="590"
        y="190"
        text-anchor="middle"
      >funded startups</text>
      <text
        class="blue-sub"
        x="590"
        y="208"
        text-anchor="middle"
      >pricing scales up</text>
      <text
        class="blue-sub"
        x="590"
        y="224"
        text-anchor="middle"
      >quickly</text>

      <text
        class="hint"
        x="340"
        y="278"
        text-anchor="middle"
      >Click a card to learn more</text>
    </svg>
  </div>
</template>

<script setup></script>

<style scoped>
.cms-diagram { border-radius: 8px; overflow: hidden; }
svg text { font-family: sans-serif; font-size: 12px; }

.hint { font-size: 12px; fill: light-dark(rgba(0,0,0,0.35), rgba(255,255,255,0.35)); }

.teal-box   { fill: light-dark(#E1F5EE, #04342C); stroke: #1D9E75; stroke-width: 0.5; }
.teal-title { font-size: 14px; font-weight: 500; fill: light-dark(#085041, #5DCAA5); }
.teal-sub   { fill: light-dark(#0F6E56, #1D9E75); }
.divider    { stroke: light-dark(rgba(29,158,117,0.4), rgba(29,158,117,0.4)); stroke-width: 0.5; }

.purple-box   { fill: light-dark(#EEEDFE, #26215C); stroke: #7F77DD; stroke-width: 0.5; }
.purple-title { font-size: 14px; font-weight: 500; fill: light-dark(#3C3489, #AFA9EC); }
.purple-sub   { fill: light-dark(#534AB7, #7F77DD); }
.divider-purple { stroke: light-dark(rgba(127,119,221,0.4), rgba(127,119,221,0.4)); stroke-width: 0.5; }

.amber-box   { fill: light-dark(#FAEEDA, #412402); stroke: #BA7517; stroke-width: 0.5; }
.amber-title { font-size: 14px; font-weight: 500; fill: light-dark(#633806, #EF9F27); }
.amber-sub   { fill: light-dark(#854F0B, #BA7517); }
.divider-amber { stroke: light-dark(rgba(186,117,23,0.4), rgba(186,117,23,0.4)); stroke-width: 0.5; }

.blue-box   { fill: light-dark(#E6F1FB, #042C53); stroke: #378ADD; stroke-width: 0.5; }
.blue-title { font-size: 14px; font-weight: 500; fill: light-dark(#0C447C, #85B7EB); }
.blue-sub   { fill: light-dark(#185FA5, #378ADD); }
.divider-blue { stroke: light-dark(rgba(55,138,221,0.4), rgba(55,138,221,0.4)); stroke-width: 0.5; }
</style>
