<template>
  <div class="diagram-wrap">
    <svg
      viewBox="0 0 680 320"
      role="img"
      aria-label="Before and after comparison: custom vanilla SSR with separate Vue app instances per component versus Nuxt standard SSR with one app tree"
    >
      <defs>
        <marker
          id="fe-arrow"
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
            stroke="currentColor"
            stroke-width="1.5"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </marker>
      </defs>

      <g class="panel before">
        <rect
          x="30"
          y="30"
          width="290"
          height="260"
          rx="20"
        />
        <text
          class="heading"
          x="175"
          y="58"
          text-anchor="middle"
        >Before</text>
        <text
          class="subtitle"
          x="175"
          y="76"
          text-anchor="middle"
        >Custom vanilla SSR</text>
      </g>
      <g class="chip before">
        <rect
          x="55"
          y="95"
          width="100"
          height="50"
          rx="10"
        />
        <text
          class="subtitle"
          x="105"
          y="120"
          text-anchor="middle"
          dominant-baseline="central"
        >App A</text>
      </g>
      <g class="chip before">
        <rect
          x="165"
          y="95"
          width="100"
          height="50"
          rx="10"
        />
        <text
          class="subtitle"
          x="215"
          y="120"
          text-anchor="middle"
          dominant-baseline="central"
        >App B</text>
      </g>
      <g class="chip before">
        <rect
          x="110"
          y="155"
          width="100"
          height="50"
          rx="10"
        />
        <text
          class="subtitle"
          x="160"
          y="180"
          text-anchor="middle"
          dominant-baseline="central"
        >App C</text>
      </g>
      <text
        class="subtitle"
        x="175"
        y="230"
        text-anchor="middle"
      >Every component = own Vue app</text>
      <text
        class="subtitle"
        x="175"
        y="250"
        text-anchor="middle"
      >Compile: minutes · no hot reload</text>

      <g class="panel after">
        <rect
          x="360"
          y="30"
          width="290"
          height="260"
          rx="20"
        />
        <text
          class="heading"
          x="505"
          y="58"
          text-anchor="middle"
        >After</text>
        <text
          class="subtitle"
          x="505"
          y="76"
          text-anchor="middle"
        >Nuxt standard SSR</text>
      </g>
      <g class="chip after">
        <rect
          x="440"
          y="100"
          width="130"
          height="100"
          rx="12"
        />
        <text
          class="title"
          x="505"
          y="130"
          text-anchor="middle"
          dominant-baseline="central"
        >One app tree</text>
        <text
          class="subtitle"
          x="505"
          y="150"
          text-anchor="middle"
          dominant-baseline="central"
        >A + B + C</text>
        <text
          class="subtitle"
          x="505"
          y="168"
          text-anchor="middle"
          dominant-baseline="central"
        >as components</text>
      </g>
      <text
        class="subtitle"
        x="505"
        y="230"
        text-anchor="middle"
      >Compile: seconds · hot reload works</text>

      <line
        x1="320"
        y1="160"
        x2="358"
        y2="160"
        class="arr"
        marker-end="url(#fe-arrow)"
      />
    </svg>
  </div>
</template>

<style scoped>
.diagram-wrap {
  width: 100%;
  margin: 1.5rem 0;
  border-radius: 12px;
  padding: 1rem;
  background: light-dark(#fafafa, #171717);
  border: 1px solid light-dark(#e5e5e5, #404040);
}

svg {
  width: 100%;
  height: auto;
  display: block;
  color: light-dark(#171717, #f5f5f5);
}

.heading {
  font-size: 14px;
  font-weight: 500;
  fill: light-dark(#171717, #f5f5f5);
}

.title {
  font-size: 14px;
  font-weight: 500;
}

.subtitle {
  font-size: 12px;
  fill: light-dark(#737373, #a3a3a3);
}

.panel.before rect {
  fill: light-dark(#fef2f2, #450a0a);
  stroke: light-dark(#f87171, #ef4444);
  stroke-width: 0.5;
}

.panel.after rect {
  fill: light-dark(#eff6ff, #1e3a8a);
  stroke: light-dark(#3b82f6, #60a5fa);
  stroke-width: 0.5;
}

.chip.before rect {
  fill: light-dark(#fecaca, #7f1d1d);
  stroke: light-dark(#ef4444, #f87171);
  stroke-width: 0.5;
}

.chip.before text {
  fill: light-dark(#991b1b, #fecaca);
}

.chip.after rect {
  fill: light-dark(#bfdbfe, #1e40af);
  stroke: light-dark(#2563eb, #60a5fa);
  stroke-width: 0.5;
}

.chip.after .title {
  fill: light-dark(#1e3a8a, #dbeafe);
}

.chip.after .subtitle {
  fill: light-dark(#1e40af, #bfdbfe);
}

.arr {
  stroke: currentColor;
  stroke-width: 1;
}
</style>
