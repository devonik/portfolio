<template>
  <div class="crawl-architecture my-8">
    <svg width="100%" viewBox="0 0 680 420" role="img" xmlns="http://www.w3.org/2000/svg">
      <title>Two-phase crawling architecture for GoSpendl</title>
      <desc>Phase 1: LLM schema discovery once per shop. Phase 2: CSS extraction for every production crawl with zero LLM calls.</desc>

      <defs>
        <marker id="arch-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M2 1L8 5L2 9" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </marker>
      </defs>

      <!-- Phase 1 container -->
      <rect x="40" y="36" width="270" height="340" rx="8" fill="none" :stroke="borderColor" stroke-width="0.5" stroke-dasharray="5,4"/>
      <text x="175" y="26" font-size="12" text-anchor="middle" :fill="subtitleColor" font-family="sans-serif">Phase 1 — schema discovery (once per shop)</text>

      <!-- Phase 2 container -->
      <rect x="370" y="36" width="270" height="340" rx="8" fill="none" :stroke="borderColor" stroke-width="0.5" stroke-dasharray="5,4"/>
      <text x="505" y="26" font-size="12" text-anchor="middle" :fill="subtitleColor" font-family="sans-serif">Phase 2 — production crawl (no LLM)</text>

      <!-- Phase 1: Shop search page -->
      <rect x="65" y="56" width="220" height="50" rx="4" :fill="tealFill" :stroke="tealStroke" stroke-width="0.5"/>
      <text x="175" y="77" font-size="14" font-weight="500" text-anchor="middle" :fill="tealText" font-family="sans-serif">Shop search page</text>
      <text x="175" y="95" font-size="12" text-anchor="middle" :fill="tealText" font-family="sans-serif" opacity="0.85">e.g. baur.de/s/ipad</text>

      <line x1="175" y1="106" x2="175" y2="132" :stroke="arrowColor" stroke-width="0.5" marker-end="url(#arch-arrow)"/>

      <!-- Phase 1: Crawl4AI -->
      <rect x="65" y="134" width="220" height="50" rx="4" :fill="blueFill" :stroke="blueStroke" stroke-width="0.5"/>
      <text x="175" y="155" font-size="14" font-weight="500" text-anchor="middle" :fill="blueText" font-family="sans-serif">Crawl4AI</text>
      <text x="175" y="173" font-size="12" text-anchor="middle" :fill="blueText" font-family="sans-serif" opacity="0.85">renders full page, raw HTML</text>

      <line x1="175" y1="184" x2="175" y2="210" :stroke="arrowColor" stroke-width="0.5" marker-end="url(#arch-arrow)"/>

      <!-- Phase 1: Gemini -->
      <rect x="65" y="212" width="220" height="50" rx="4" :fill="amberFill" :stroke="amberStroke" stroke-width="0.5"/>
      <text x="175" y="233" font-size="14" font-weight="500" text-anchor="middle" :fill="amberText" font-family="sans-serif">Gemini Flash Lite</text>
      <text x="175" y="251" font-size="12" text-anchor="middle" :fill="amberText" font-family="sans-serif" opacity="0.85">generates CSS schema from HTML</text>

      <line x1="175" y1="262" x2="175" y2="288" :stroke="arrowColor" stroke-width="0.5" marker-end="url(#arch-arrow)"/>

      <!-- Phase 1: store-overrides.json -->
      <rect x="65" y="290" width="220" height="50" rx="4" :fill="greenFill" :stroke="greenStroke" stroke-width="0.5"/>
      <text x="175" y="311" font-size="14" font-weight="500" text-anchor="middle" :fill="greenText" font-family="sans-serif">store-overrides.json</text>
      <text x="175" y="329" font-size="12" text-anchor="middle" :fill="greenText" font-family="sans-serif" opacity="0.85">schema stored per shop</text>

      <!-- Horizontal arrow: Phase 1 → Phase 2 -->
      <line x1="285" y1="315" x2="370" y2="315" :stroke="arrowColor" stroke-width="0.5" stroke-dasharray="4,3" marker-end="url(#arch-arrow)"/>
      <text x="327" y="308" font-size="11" text-anchor="middle" :fill="subtitleColor" font-family="sans-serif">reused</text>

      <!-- Phase 2: User search -->
      <rect x="395" y="56" width="220" height="50" rx="4" :fill="tealFill" :stroke="tealStroke" stroke-width="0.5"/>
      <text x="505" y="77" font-size="14" font-weight="500" text-anchor="middle" :fill="tealText" font-family="sans-serif">User searches "toaster"</text>
      <text x="505" y="95" font-size="12" text-anchor="middle" :fill="tealText" font-family="sans-serif" opacity="0.85">POST /api/crawl</text>

      <line x1="505" y1="106" x2="505" y2="132" :stroke="arrowColor" stroke-width="0.5" marker-end="url(#arch-arrow)"/>

      <!-- Phase 2: Crawl4AI CSS -->
      <rect x="395" y="134" width="220" height="50" rx="4" :fill="blueFill" :stroke="blueStroke" stroke-width="0.5"/>
      <text x="505" y="155" font-size="14" font-weight="500" text-anchor="middle" :fill="blueText" font-family="sans-serif">Crawl4AI</text>
      <text x="505" y="173" font-size="12" text-anchor="middle" :fill="blueText" font-family="sans-serif" opacity="0.85">CSS extraction, zero LLM calls</text>

      <line x1="505" y1="184" x2="505" y2="210" :stroke="arrowColor" stroke-width="0.5" marker-end="url(#arch-arrow)"/>

      <!-- Phase 2: Webhook -->
      <rect x="395" y="212" width="220" height="50" rx="4" :fill="purpleFill" :stroke="purpleStroke" stroke-width="0.5"/>
      <text x="505" y="233" font-size="14" font-weight="500" text-anchor="middle" :fill="purpleText" font-family="sans-serif">Webhook</text>
      <text x="505" y="251" font-size="12" text-anchor="middle" :fill="purpleText" font-family="sans-serif" opacity="0.85">normalize price, name, URLs</text>

      <line x1="505" y1="262" x2="505" y2="288" :stroke="arrowColor" stroke-width="0.5" marker-end="url(#arch-arrow)"/>

      <!-- Phase 2: Algolia -->
      <rect x="395" y="290" width="220" height="50" rx="4" :fill="greenFill" :stroke="greenStroke" stroke-width="0.5"/>
      <text x="505" y="311" font-size="14" font-weight="500" text-anchor="middle" :fill="greenText" font-family="sans-serif">Algolia</text>
      <text x="505" y="329" font-size="12" text-anchor="middle" :fill="greenText" font-family="sans-serif" opacity="0.85">products indexed, ready to search</text>

      <!-- Legend -->
      <rect x="65" y="364" width="12" height="12" rx="2" :fill="blueFill" :stroke="blueStroke" stroke-width="0.5"/>
      <text x="83" y="374" font-size="11" :fill="subtitleColor" font-family="sans-serif">Crawl4AI</text>

      <rect x="175" y="364" width="12" height="12" rx="2" :fill="amberFill" :stroke="amberStroke" stroke-width="0.5"/>
      <text x="193" y="374" font-size="11" :fill="subtitleColor" font-family="sans-serif">LLM (phase 1 only)</text>

      <rect x="320" y="364" width="12" height="12" rx="2" :fill="greenFill" :stroke="greenStroke" stroke-width="0.5"/>
      <text x="338" y="374" font-size="11" :fill="subtitleColor" font-family="sans-serif">persisted / indexed</text>

      <rect x="480" y="364" width="12" height="12" rx="2" :fill="purpleFill" :stroke="purpleStroke" stroke-width="0.5"/>
      <text x="498" y="374" font-size="11" :fill="subtitleColor" font-family="sans-serif">normalization</text>
    </svg>
  </div>
</template>

<script setup>
const isDark = typeof window !== 'undefined'
  ? window.matchMedia('(prefers-color-scheme: dark)').matches
  : false

const borderColor  = isDark ? 'rgba(255,255,255,0.2)' : 'rgba(0,0,0,0.2)'
const arrowColor   = isDark ? 'rgba(255,255,255,0.35)' : 'rgba(0,0,0,0.35)'
const subtitleColor = isDark ? 'rgba(255,255,255,0.5)' : 'rgba(0,0,0,0.45)'

const tealFill   = isDark ? '#0d3d3a' : '#e6f7f6'
const tealStroke = isDark ? '#2a9d8f' : '#2a9d8f'
const tealText   = isDark ? '#5ecfbf' : '#1a6b63'

const blueFill   = isDark ? '#0d2d4a' : '#e6f0fa'
const blueStroke = isDark ? '#3a7bbf' : '#3a7bbf'
const blueText   = isDark ? '#6ab0f0' : '#1a4a7a'

const amberFill   = isDark ? '#3d2a00' : '#fff8e6'
const amberStroke = isDark ? '#d4920a' : '#d4920a'
const amberText   = isDark ? '#f0c060' : '#7a4f00'

const greenFill   = isDark ? '#0d3320' : '#e8f7ee'
const greenStroke = isDark ? '#2d9a50' : '#2d9a50'
const greenText   = isDark ? '#5ecf85' : '#1a5c33'

const purpleFill   = isDark ? '#2d1a4a' : '#f0ebfa'
const purpleStroke = isDark ? '#7a50c0' : '#7a50c0'
const purpleText   = isDark ? '#b090e8' : '#4a2880'
</script>

<style scoped>
.crawl-architecture {
  border-radius: 8px;
  overflow: hidden;
}
</style>
