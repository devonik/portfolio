<script setup lang="ts">
const { data: page } = await useAsyncData('privacy', () => {
  return queryCollection('privacy').first()
})
if (!page.value) {
  throw createError({
    statusCode: 404,
    statusMessage: 'Page not found',
    fatal: true
  })
}

useSeoMeta({
  title: page.value?.seo?.title || page.value?.title,
  ogTitle: page.value?.seo?.title || page.value?.title,
  description: page.value?.seo?.description || page.value?.description,
  ogDescription: page.value?.seo?.description || page.value?.description
})
</script>

<template>
  <UPage v-if="page">
    <UPageHero
      :title="page.title"
      :description="page.description"
      orientation="horizontal"
      :ui="{
        container: 'lg:flex sm:flex-row items-center',
        title: '!mx-0 text-left',
        description: '!mx-0 text-left',
        links: 'justify-start'
      }"
    />
    <UPageSection
      :ui="{
        container: '!pt-0'
      }"
    >
      <div class="prose dark:prose-invert max-w-none">
        <MDC
          :value="page.content"
          unwrap="p"
        />
        <p
          v-if="page.lastUpdated"
          class="text-sm text-muted mt-12"
        >
          Last updated: {{ new Date(page.lastUpdated).toLocaleDateString() }}
        </p>
      </div>
    </UPageSection>
  </UPage>
</template>
