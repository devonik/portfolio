<template>
  <div class="diagram-wrap">
    <svg viewBox="0 0 680 320" role="img" aria-label="Crawl webhook publishes to Upstash Redis, which fans out to SSE subscribers on two separate serverless instances, one of which streams to the connected browser client">
      <defs>
        <marker id="sse-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M2 1L8 5L2 9" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
        </marker>
      </defs>

      <g class="node source">
        <rect x="20" y="30" width="180" height="50" rx="8" />
        <text class="title" x="110" y="50" text-anchor="middle" dominant-baseline="central">Crawl webhook</text>
        <text class="subtitle" x="110" y="68" text-anchor="middle" dominant-baseline="central">publishes via REST</text>
      </g>

      <line x1="200" y1="55" x2="260" y2="55" class="arr" marker-end="url(#sse-arrow)" />

      <g class="node redis">
        <rect x="260" y="30" width="160" height="50" rx="8" />
        <text class="title" x="340" y="50" text-anchor="middle" dominant-baseline="central">Upstash Redis</text>
        <text class="subtitle" x="340" y="68" text-anchor="middle" dominant-baseline="central">crawl:events:env</text>
      </g>

      <path d="M300 80 L150 190" fill="none" class="arr" marker-end="url(#sse-arrow)" />
      <path d="M380 80 L500 190" fill="none" class="arr" marker-end="url(#sse-arrow)" />

      <g class="node instance">
        <rect x="40" y="192" width="220" height="60" rx="8" />
        <text class="title" x="150" y="212" text-anchor="middle" dominant-baseline="central">Instance A</text>
        <text class="subtitle" x="150" y="232" text-anchor="middle" dominant-baseline="central">SSE subscriber, no client</text>
      </g>

      <g class="node instance active">
        <rect x="400" y="192" width="220" height="60" rx="8" />
        <text class="title" x="510" y="212" text-anchor="middle" dominant-baseline="central">Instance B</text>
        <text class="subtitle" x="510" y="232" text-anchor="middle" dominant-baseline="central">SSE subscriber, client attached</text>
      </g>

      <line x1="510" y1="252" x2="510" y2="280" class="arr" marker-end="url(#sse-arrow)" />

      <g class="node client">
        <rect x="410" y="282" width="200" height="34" rx="17" />
        <text class="subtitle" x="510" y="299" text-anchor="middle" dominant-baseline="central">Browser on /search</text>
      </g>

      <text class="caption" x="150" y="286" text-anchor="middle">Publish and subscribe never share an instance</text>
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

.title {
  font-size: 14px;
  font-weight: 500;
  fill: light-dark(#171717, #f5f5f5);
}

.subtitle {
  font-size: 12px;
  fill: light-dark(#737373, #a3a3a3);
}

.caption {
  font-size: 12px;
  fill: light-dark(#737373, #a3a3a3);
}

.node.source rect {
  fill: light-dark(#f5f5f5, #262626);
  stroke: light-dark(#a3a3a3, #737373);
  stroke-width: 0.5;
}

.node.redis rect {
  fill: light-dark(#fef2f2, #450a0a);
  stroke: light-dark(#f87171, #ef4444);
  stroke-width: 1;
}

.node.redis .title,
.node.redis .subtitle {
  fill: light-dark(#991b1b, #fecaca);
}

.node.instance rect {
  fill: light-dark(#f5f5f5, #262626);
  stroke: light-dark(#d4d4d4, #525252);
  stroke-width: 0.5;
}

.node.instance.active rect {
  fill: light-dark(#eff6ff, #1e3a8a);
  stroke: light-dark(#3b82f6, #60a5fa);
  stroke-width: 1;
}

.node.instance.active .title,
.node.instance.active .subtitle {
  fill: light-dark(#1e40af, #dbeafe);
}

.node.client rect {
  fill: light-dark(#eff6ff, #1e40af);
  stroke: light-dark(#3b82f6, #93c5fd);
  stroke-width: 0.5;
}

.arr {
  stroke: currentColor;
  stroke-width: 1;
  opacity: 0.7;
}
</style>
