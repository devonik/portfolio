export default defineAppConfig({
  global: {
    picture: {
      dark: '/profile.jpg',
      light: '/profile.jpg',
      alt: 'My profile picture'
    },
    meetingLink: 'https://cal.com/devnik',
    email: 'niklas.grieger@devnik.dev',
    available: true
  },
  ui: {
    colors: {
      primary: 'blue',
      neutral: 'neutral'
    },
    pageHero: {
      slots: {
        container: 'gap-3 sm:gap-3 py-18 sm:py-24 lg:py-32',
        title: 'mx-auto max-w-xl text-pretty text-3xl sm:text-4xl lg:text-5xl',
        description: 'mt-2 text-md mx-auto max-w-2xl text-pretty sm:text-md text-muted'
      }
    }
  },
  footer: {
    credits: `Created by Niklas Grieger • © 2025`,
    colorMode: false,
    links: [{
      'icon': 'i-lucide-mail',
      'to': 'mailto:niklas.grieger@devnik.dev',
      'aria-label': 'Email'
    }, {
      'icon': 'i-lucide-linkedin',
      'to': 'https://www.linkedin.com/in/niklas-grieger-b98086152/',
      'target': '_blank',
      'aria-label': 'LinkedIn'
    }, {
      'icon': 'i-simple-icons-github',
      'to': 'https://github.com/devonik',
      'target': '_blank',
      'aria-label': 'GitHub'
    }, {
      'icon': 'i-simple-icons-stackoverflow',
      'to': 'https://stackoverflow.com/users/6143720/devnik',
      'target': '_blank',
      'aria-label': 'GitHub'
    }, {
      'icon': 'i-simple-icons-npm',
      'to': 'https://www.npmjs.com/~devnik',
      'target': '_blank',
      'aria-label': 'GitHub'
    }]
  }
})
