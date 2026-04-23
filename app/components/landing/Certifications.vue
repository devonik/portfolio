<script setup lang="ts">
import type { IndexCollectionItem } from '@nuxt/content'

defineProps<{
  page: IndexCollectionItem
}>()
</script>

<template>
  <UPageSection
    :title="page.certifications.title"
    :description="page.certifications.description"
    :ui="{
      container: '!p-0 gap-4 sm:gap-4',
      title: 'text-left text-xl sm:text-xl lg:text-2xl font-medium',
      description: 'text-left mt-2 text-sm sm:text-md lg:text-sm text-muted'
    }"
  >
    <div class="flex flex-wrap gap-3">
      <Motion
        v-for="(cert, index) in page.certifications.items"
        :key="index"
        :initial="{ opacity: 0, transform: 'translateY(20px)' }"
        :while-in-view="{ opacity: 1, transform: 'translateY(0)' }"
        :transition="{ delay: 0.1 * index }"
        :in-view-options="{ once: true }"
      >
        <ULink
          :to="cert.url"
          target="_blank"
          class="group inline-flex items-center gap-2 rounded-full bg-elevated/50 ring ring-default px-3 py-1.5 transition hover:bg-elevated hover:ring-accented"
        >
          <UIcon
            :name="cert.icon"
            class="size-4"
            :style="{ color: cert.color }"
          />
          <span class="text-sm font-medium text-default">{{ cert.name }}</span>
          <UBadge
            :label="cert.level"
            size="sm"
            variant="subtle"
            color="primary"
          />
        </ULink>
      </Motion>
    </div>
  </UPageSection>
</template>
