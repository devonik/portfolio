// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: [
    '@nuxt/eslint',
    '@nuxt/image',
    '@nuxt/ui',
    '@nuxt/content',
    '@vueuse/nuxt',
    '@nuxtjs/seo',
    'motion-v/nuxt'
  ],

  devtools: {
    enabled: true
  },

  css: ['~/assets/css/main.css'],

  site: {
    url: process.env.NUXT_SITE_URL || 'https://devnik.dev',
    name: process.env.NUXT_SITE_NAME || 'Niklas Grieger',
    description: 'Senior Full Stack Engineer specializing in Vue, Nuxt, Node.js & AWS. Available for remote freelance.',
    defaultLocale: 'en'
  },
  runtimeConfig: {
    site: {
      url: process.env.NUXT_SITE_URL,
      name: process.env.NUXT_SITE_NAME
    }
  },

  compatibilityDate: '2024-11-01',

  nitro: {
    prerender: {
      routes: [
        '/'
      ],
      crawlLinks: true
    }
  },

  eslint: {
    config: {
      stylistic: {
        commaDangle: 'never',
        braceStyle: '1tbs'
      }
    }
  }
})
