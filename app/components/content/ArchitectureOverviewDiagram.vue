<template>
  <div class="diagram-wrap">
    <svg viewBox="0 0 680 350" role="img" aria-label="Architecture overview: four frontends connecting to four backend services, shop backend on Node.js and PMS service, termine service, and excel service on Java Spring Boot, with a legacy backend used only by the webshop">
      <defs>
        <marker id="arch-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M2 1L8 5L2 9" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
        </marker>
      </defs>

      <g class="node frontend">
        <rect x="20" y="30" width="150" height="44" rx="8" />
        <text class="title" x="95" y="52" text-anchor="middle" dominant-baseline="central">Webshop</text>
      </g>
      <g class="node frontend">
        <rect x="180" y="30" width="150" height="44" rx="8" />
        <text class="title" x="255" y="52" text-anchor="middle" dominant-baseline="central">PMS frontend</text>
      </g>
      <g class="node frontend">
        <rect x="340" y="30" width="150" height="44" rx="8" />
        <text class="title" x="415" y="52" text-anchor="middle" dominant-baseline="central">Pet owner portal</text>
      </g>
      <g class="node frontend">
        <rect x="500" y="30" width="150" height="44" rx="8" />
        <text class="title" x="575" y="52" text-anchor="middle" dominant-baseline="central">Supplier admin</text>
      </g>

      <line x1="95" y1="74" x2="95" y2="208" class="arr" marker-end="url(#arch-arrow)" />
      <line x1="255" y1="74" x2="255" y2="208" class="arr" marker-end="url(#arch-arrow)" />
      <line x1="415" y1="74" x2="415" y2="208" class="arr" marker-end="url(#arch-arrow)" />
      <line x1="575" y1="74" x2="575" y2="208" class="arr" marker-end="url(#arch-arrow)" />

      <path d="M415 74 L140 208" fill="none" class="arr dashed" marker-end="url(#arch-arrow)" />
      <path d="M575 74 L120 208" fill="none" class="arr dashed" marker-end="url(#arch-arrow)" />

      <g class="node backend node-node">
        <rect x="20" y="210" width="150" height="56" rx="8" />
        <text class="title" x="95" y="230" text-anchor="middle" dominant-baseline="central">Shop backend</text>
        <text class="subtitle" x="95" y="248" text-anchor="middle" dominant-baseline="central">Node.js</text>
      </g>
      <g class="node backend orchestrator">
        <rect x="180" y="210" width="150" height="56" rx="8" />
        <text class="title" x="255" y="230" text-anchor="middle" dominant-baseline="central">PMS service</text>
        <text class="subtitle" x="255" y="248" text-anchor="middle" dominant-baseline="central">Java, Spring Boot</text>
      </g>
      <g class="node backend java-node">
        <rect x="340" y="210" width="150" height="56" rx="8" />
        <text class="title" x="415" y="230" text-anchor="middle" dominant-baseline="central">Termine service</text>
        <text class="subtitle" x="415" y="248" text-anchor="middle" dominant-baseline="central">Java, Spring Boot</text>
      </g>
      <g class="node backend java-node">
        <rect x="500" y="210" width="150" height="56" rx="8" />
        <text class="title" x="575" y="230" text-anchor="middle" dominant-baseline="central">Excel service</text>
        <text class="subtitle" x="575" y="248" text-anchor="middle" dominant-baseline="central">Java, Spring Boot</text>
      </g>

      <g class="node legacy">
        <rect x="20" y="290" width="150" height="34" rx="6" stroke-dasharray="3 3" />
        <text class="subtitle" x="95" y="307" text-anchor="middle" dominant-baseline="central">Legacy backend</text>
      </g>
      <text class="subtitle" x="95" y="284" text-anchor="middle">Webshop only, partial</text>

      <text class="caption" x="340" y="342" text-anchor="middle">Solid = primary connection · Dashed = secondary · Simplified overview</text>
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

.node.frontend rect {
  fill: light-dark(#f5f5f5, #262626);
  stroke: light-dark(#a3a3a3, #737373);
  stroke-width: 0.5;
}

.node.backend rect {
  fill: light-dark(#eff6ff, #1e3a8a);
  stroke: light-dark(#3b82f6, #60a5fa);
  stroke-width: 0.5;
}

.node.backend .title,
.node.backend .subtitle {
  fill: light-dark(#1e40af, #dbeafe);
}

.node.orchestrator rect {
  fill: light-dark(#dbeafe, #1e40af);
  stroke: light-dark(#2563eb, #93c5fd);
  stroke-width: 1;
}

.node.orchestrator .title,
.node.orchestrator .subtitle {
  fill: light-dark(#1e3a8a, #eff6ff);
}

.node.legacy rect {
  fill: light-dark(#f5f5f5, #262626);
  stroke: light-dark(#d4d4d4, #525252);
  stroke-width: 0.5;
}

.arr {
  stroke: currentColor;
  stroke-width: 0.5;
  opacity: 0.6;
}

.arr.dashed {
  stroke-dasharray: 4 3;
  opacity: 0.5;
}
</style>
