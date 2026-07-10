<template>
  <div class="diagram-wrap">
    <svg
      viewBox="0 0 680 260"
      role="img"
      aria-label="Blue/green reindex state machine: Collect, CreateIndex, Insert, UpdateAlias, with a shared Failed cleanup path"
    >
      <defs>
        <marker
          id="bg-arrow"
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
            :stroke="strokeColor"
            stroke-width="1.5"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </marker>
      </defs>

      <g class="node">
        <rect
          x="30"
          y="40"
          width="130"
          height="56"
          rx="8"
        />
        <text
          class="title"
          x="95"
          y="60"
          text-anchor="middle"
          dominant-baseline="central"
        >Collect</text>
        <text
          class="subtitle"
          x="95"
          y="78"
          text-anchor="middle"
          dominant-baseline="central"
        >Stage data in S3</text>
      </g>

      <g class="node">
        <rect
          x="185"
          y="40"
          width="140"
          height="56"
          rx="8"
        />
        <text
          class="title"
          x="255"
          y="60"
          text-anchor="middle"
          dominant-baseline="central"
        >Create index</text>
        <text
          class="subtitle"
          x="255"
          y="78"
          text-anchor="middle"
          dominant-baseline="central"
        >New timestamped index</text>
      </g>

      <g class="node">
        <rect
          x="350"
          y="40"
          width="130"
          height="56"
          rx="8"
        />
        <text
          class="title"
          x="415"
          y="60"
          text-anchor="middle"
          dominant-baseline="central"
        >Insert</text>
        <text
          class="subtitle"
          x="415"
          y="78"
          text-anchor="middle"
          dominant-baseline="central"
        >Bulk insert in batches</text>
      </g>

      <g class="node accent">
        <rect
          x="505"
          y="40"
          width="145"
          height="56"
          rx="8"
        />
        <text
          class="title"
          x="577"
          y="60"
          text-anchor="middle"
          dominant-baseline="central"
        >Update alias</text>
        <text
          class="subtitle"
          x="577"
          y="78"
          text-anchor="middle"
          dominant-baseline="central"
        >Atomic switch, cleanup old</text>
      </g>

      <line
        x1="160"
        y1="68"
        x2="183"
        y2="68"
        class="arr"
        marker-end="url(#bg-arrow)"
      />
      <line
        x1="325"
        y1="68"
        x2="348"
        y2="68"
        class="arr"
        marker-end="url(#bg-arrow)"
      />
      <line
        x1="480"
        y1="68"
        x2="503"
        y2="68"
        class="arr"
        marker-end="url(#bg-arrow)"
      />

      <line
        x1="95"
        y1="96"
        x2="95"
        y2="175"
        class="arr faint"
      />
      <line
        x1="255"
        y1="96"
        x2="255"
        y2="175"
        class="arr faint"
      />
      <line
        x1="415"
        y1="96"
        x2="415"
        y2="175"
        class="arr faint"
      />
      <line
        x1="577"
        y1="96"
        x2="577"
        y2="175"
        class="arr faint"
      />

      <path
        d="M95 175 L577 175"
        fill="none"
        class="connector"
      />
      <path
        d="M340 175 L340 194"
        fill="none"
        class="connector"
        marker-end="url(#bg-arrow)"
      />

      <g class="node danger">
        <rect
          x="275"
          y="196"
          width="130"
          height="56"
          rx="8"
        />
        <text
          class="title"
          x="340"
          y="216"
          text-anchor="middle"
          dominant-baseline="central"
        >Failed</text>
        <text
          class="subtitle"
          x="340"
          y="234"
          text-anchor="middle"
          dominant-baseline="central"
        >Cleanup + Slack alert</text>
      </g>

      <text
        class="subtitle"
        x="340"
        y="163"
        text-anchor="middle"
      >catch on any step</text>
    </svg>
  </div>
</template>

<script setup>
const strokeColor = 'light-dark(#171717, #f5f5f5)'
</script>

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
}

.title {
  font-size: 14px;
  font-weight: 500;
  fill: light-dark(#171717, #f5f5f5);
}

.subtitle {
  font-size: 12px;
  fill: light-dark(#737373, #a3a3a3);
}

.node rect {
  fill: light-dark(#f5f5f5, #262626);
  stroke: light-dark(#d4d4d4, #525252);
  stroke-width: 0.5;
}

.node.accent rect {
  fill: light-dark(#eff6ff, #1e3a8a);
  stroke: light-dark(#3b82f6, #60a5fa);
}

.node.accent .title,
.node.accent .subtitle {
  fill: light-dark(#1e40af, #dbeafe);
}

.node.danger rect {
  fill: light-dark(#fef2f2, #7f1d1d);
  stroke: light-dark(#f87171, #ef4444);
}

.node.danger .title,
.node.danger .subtitle {
  fill: light-dark(#991b1b, #fee2e2);
}

.arr {
  stroke: light-dark(#171717, #f5f5f5);
  stroke-width: 1;
}

.arr.faint {
  stroke: light-dark(#171717, #f5f5f5);
  stroke-width: 1;
  opacity: 0.4;
}

.connector {
  stroke: light-dark(#171717, #f5f5f5);
  stroke-width: 0.5;
  opacity: 0.5;
}
</style>
