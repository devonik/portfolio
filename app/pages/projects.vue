<script setup lang="ts">
const { data: page } = await useAsyncData('projects-page', () => {
  return queryCollection('pages').path('/projects').first()
})
if (!page.value) {
  throw createError({
    statusCode: 404,
    statusMessage: 'Page not found',
    fatal: true
  })
}

const { data: projects } = await useAsyncData('projects', () => {
  return queryCollection('projects').all()
})

const { global } = useAppConfig()

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
      :links="page.links"
      :ui="{
        title: '!mx-0 text-left',
        description: '!mx-0 text-left',
        links: 'justify-start'
      }"
    >
      <template #links>
        <div
          v-if="page.links"
          class="flex items-center gap-2"
        >
          <UButton
            :label="page.links[0]?.label"
            :to="global.meetingLink"
            v-bind="page.links[0]"
          />
          <UButton
            :to="`mailto:${global.email}`"
            v-bind="page.links[1]"
          />
        </div>
      </template>
    </UPageHero>
    <UPageSection
      :ui="{
        container: '!pt-0'
      }"
    >
      <template
        v-for="(project, index) in projects"
        :key="project.title"
      >
        <Motion
          :initial="{ opacity: 0, transform: 'translateY(10px)' }"
          :while-in-view="{ opacity: 1, transform: 'translateY(0)' }"
          :transition="{ delay: 0.2 * index }"
          :in-view-options="{ once: true }"
        >
          <UPageCard
            :title="project.title"
            :description="project.description"
            orientation="vertical"
            variant="naked"
            class="group text-center"
            :ui="{
              title: 'text-center',
              description: 'text-center',
              footer: 'justify-center'
            }"
          >
            <template #leading>
              <div class="flex items-center justify-center gap-2">
                <span class="text-sm text-muted">
                  {{ project.period || new Date(project.date).getUTCFullYear() }}
                </span>
                <UBadge
                  v-if="project.type"
                  :label="project.type === 'client' ? 'Client project' : 'Private project'"
                  :icon="project.type === 'client' ? 'i-lucide-briefcase' : 'i-lucide-user'"
                  :color="project.type === 'client' ? 'primary' : 'neutral'"
                  variant="soft"
                  size="sm"
                />
              </div>
            </template>
            <template #footer>
              <div class="flex items-center justify-center gap-4">
                <NuxtLink
                  v-if="project.url"
                  :to="project.url"
                  target="_blank"
                  class="text-sm text-primary flex items-center"
                >
                  View Project
                  <UIcon
                    name="i-lucide-arrow-right"
                    class="size-4 text-primary transition-all opacity-0 group-hover:translate-x-1 group-hover:opacity-100"
                  />
                </NuxtLink>
                <NuxtLink
                  v-if="project.relatedBlog"
                  :to="project.relatedBlog"
                  class="text-sm text-muted flex items-center gap-1 hover:text-primary"
                >
                  <UIcon
                    name="i-lucide-book-open"
                    class="size-4"
                  />
                  Read the case study
                </NuxtLink>
              </div>
            </template>
            <video
              v-if="project.image?.endsWith('.mp4')"
              :src="project.image"
              :aria-label="project.title"
              class="object-contain w-full max-h-80 rounded-lg mx-auto"
              autoplay
              muted
              loop
              playsinline
            />
            <img
              v-else
              :src="project.image"
              :alt="project.title"
              class="object-contain w-full max-h-80 rounded-lg mx-auto"
            >
            <ul
              v-if="project.highlights?.length"
              class="mt-4 mx-auto max-w-2xl list-disc pl-5 space-y-1 text-left text-sm text-muted"
            >
              <li
                v-for="item in project.highlights"
                :key="item"
              >
                {{ item }}
              </li>
            </ul>
            <div
              v-if="project.tech?.length"
              class="mt-4 flex flex-wrap justify-center gap-2"
            >
              <UBadge
                v-for="item in project.tech"
                :key="item.name"
                :icon="item.icon"
                :label="item.name"
                color="neutral"
                variant="subtle"
                size="sm"
              />
            </div>
          </UPageCard>
        </Motion>
        <USeparator
          v-if="projects && index < projects.length - 1"
          class="my-8"
        />
      </template>
    </UPageSection>
  </UPage>
</template>
