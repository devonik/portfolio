<script setup lang="ts">
import { Analytics } from '@vercel/analytics/nuxt'
import { SpeedInsights } from '@vercel/speed-insights/nuxt'

const colorMode = useColorMode()

const color = computed(() =>
  colorMode.value === 'dark' ? '#020618' : 'white'
)

useHead({
  meta: [
    { charset: 'utf-8' },
    { name: 'viewport', content: 'width=device-width, initial-scale=1' },
    { key: 'theme-color', name: 'theme-color', content: color }
  ],
  link: [{ rel: 'icon', href: '/favicon.ico' }],
  htmlAttrs: {
    lang: 'en'
  }
})

useSeoMeta({
  titleTemplate: '%s',
  ogImage: '/og-cover.jpg',
  twitterCard: 'summary_large_image'
})

useSchemaOrg([
  definePerson({
    name: 'Niklas Grieger',
    image: '/profile.jpg',
    jobTitle: 'Senior Full Stack Engineer',
    email: 'niklas.grieger@devnik.dev',
    url: 'https://devnik.dev',
    sameAs: [
      'https://www.linkedin.com/in/niklas-grieger-b98086152/',
      'https://github.com/devonik',
      'https://stackoverflow.com/users/6143720/devnik',
      'https://www.npmjs.com/~devnik'
    ]
  }),
  defineWebSite({
    name: 'Niklas Grieger',
    description: 'Senior Full Stack Engineer specializing in Vue, Nuxt, Node.js & AWS. Available for remote freelance.'
  }),
  defineWebPage()
])

const [{ data: navigation }, { data: files }] = await Promise.all([
  useAsyncData(
    'navigation',
    () => {
      return Promise.all([queryCollectionNavigation('blog')])
    },
    {
      transform: data => data.flat()
    }
  ),
  useLazyAsyncData(
    'search',
    () => {
      return Promise.all([queryCollectionSearchSections('blog')])
    },
    {
      server: false,
      transform: data => data.flat()
    }
  )
])
</script>

<template>
  <UApp>
    <NuxtLayout>
      <UMain class="relative">
        <NuxtPage />
      </UMain>
    </NuxtLayout>

    <ClientOnly>
      <LazyUContentSearch
        :files="files"
        :navigation="navigation"
        shortcut="meta_k"
        :links="navLinks"
        :fuse="{ resultLimit: 42 }"
      />
    </ClientOnly>

    <a
      target="_blank"
      href="https://wa.me/+4915679009238?text=Hello,%20I%20found%20you%20on%20your%20Website%20and%20I%20may%20need%20an%20developer%20for%20my%20business"
    >
      <UIcon
        class="fixed bottom-4 right-4 size-10"
        name="i-logos-whatsapp-icon"
      />
    </a>
    <Analytics />
    <SpeedInsights />
  </UApp>
</template>
