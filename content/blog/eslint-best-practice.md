---
title: "Confused by ESLint & Prettier setups: You only need ESLint for formatting and linting."
description: You want to see syntax and TypeScript errors before they happen in runtime? You want to format your code automatically with a given pattern? Then try this lightweight and easy-to-install ESLint starter template. Ready in 5 minutes. 
date: 2025-04-23
image: /blog/eslint-best-practices-hero.png
minRead: 8
author:
  name: Niklas Grieger
  avatar:
    src: /profile.jpg
    alt: Niklas Grieger
---

## My journey with ESLint and Prettier

Years ago I got in touch with ESLint as a tool for my JavaScript project. For ESLint there are tons of plugins, including an eslint-prettier plugin. And there is the tool Prettier. VSCode itself and other VSCode extensions also offer code formatters. \
All these formatters and the collaboration between them are very confusing, and I struggled to find a good and simple tutorial out there. After trying a lot, the project often became a mess, and I ended up reverting the ESLint implementation.
\
\
A very frustrating and time consuming process.
[See my solution below](#solution)

## Common problems that can be prevented or even solved by ESLint

- *Syntax errors:* We developers know the problem. Missing a "," or "{" somewhere in the code, and in runtime an unreadable JavascriptError is happening. Followed by debugging for hours to have at one point the "AHA" effect. **ESLint can show the developer these syntax errors before running the application, saving him hours of debugging and preventing critical runtime errors.**

- *TypeScript errors:* Nowadays you will find TypeScript in any modern JavaScript project, and there is a good reason for it: TypeScript allows the IDE to show the developer autocompletions and makes the project typesafe so the developer sees type errors and can fix potential runtime errors before running the application. **ESLint, with its TypeScript plugin, can automatically show your type errors within other ESLint rules.**

## Solution

After a while I started using NuxtJS (full stack framework for Vue) and I found the talented Nuxt Core developer @antfu. He built a lightweight ESLint starter template that includes many best practices.
Any config, as the ESLint rules are highly customizable, but for me this template is usable as it is.

### How to install @antfu's ESlint config in 5 minutes

> Github: <https://github.com/antfu/eslint-config>

#### Option 1: Starter Wizard

He provides a CLI tool to help you set up your project, or migrate from the legacy config to the new flat config with one command.

```bash
pnpm dlx @antfu/eslint-config@latest
```

#### Option 2: Manual Setup

If you prefer to set up manually:

```bash
pnpm i -D eslint @antfu/eslint-config
```

And create `eslint.config.mjs` in your project root:

```js
// eslint.config.mjs
import antfu from '@antfu/eslint-config'

export default antfu()
```

**Finished** EsLint with a solid ruleset is installed. Give it a try and run

Eslint dry run (show warnings, errors etc in the console)

```bash
eslint .
```

Eslint autofix (autofix code by eslint rules)

```bash
eslint . --fix
```

To run these commands in the terminal of your local machine, you need to install ESLint in your global package manager. To use the project-scoped ESLint package, you can use `npx eslint .` or add package.json scripts (recommended way).

```json
{
  "scripts": {
    ...
    "lint": "eslint .",
    "lint:fix": "eslint . --fix",
    ...
  },
}
```

### VSCode settings.json that actually works! Format your code by saving the file.

Install [VS Code ESLint extension](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)

Add the following settings to your `.vscode/settings.json`:

```jsonc
{
  // Disable the default formatter, use eslint instead
  "prettier.enable": false,
  "editor.formatOnSave": true,

  // Auto fix
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit",
    "source.organizeImports": "never"
  },

  // Silent the stylistic rules in your IDE, but still auto fix them
  "eslint.rules.customizations": [
    { "rule": "style/*", "severity": "off", "fixable": true },
    { "rule": "format/*", "severity": "off", "fixable": true },
    { "rule": "*-indent", "severity": "off", "fixable": true },
    { "rule": "*-spacing", "severity": "off", "fixable": true },
    { "rule": "*-spaces", "severity": "off", "fixable": true },
    { "rule": "*-order", "severity": "off", "fixable": true },
    { "rule": "*-dangle", "severity": "off", "fixable": true },
    { "rule": "*-newline", "severity": "off", "fixable": true },
    { "rule": "*quotes", "severity": "off", "fixable": true },
    { "rule": "*semi", "severity": "off", "fixable": true }
  ],

  // Enable eslint for all supported languages
  "eslint.validate": [
    "javascript",
    "javascriptreact",
    "typescript",
    "typescriptreact",
    "vue",
    "html",
    "markdown",
    "json",
    "jsonc",
    "yaml",
    "toml",
    "xml",
    "gql",
    "graphql",
    "astro",
    "svelte",
    "css",
    "less",
    "scss",
    "pcss",
    "postcss"
  ]
}
```

### Run ESLint before your git commit is finished (Recommended for team projects)

Especially when I am working in a team of developers, I like to keep code in the same format to prevent a mess, keep readability, and make every developer's life easier. That's a big strength of ESLint. One config and every developer can be sure the code follows a pattern.\
\
If you want to apply lint and auto-fix before every commit, you can add the following to your `package.json`:

```json
{
  "simple-git-hooks": {
    "pre-commit": "pnpm lint-staged"
  },
  "lint-staged": {
    "*": "eslint --fix"
  }
}
```

and then

```bash
npm i -D lint-staged simple-git-hooks

// to active the hooks
npx simple-git-hooks
```

These are my common tasks if I create a new project or optimize an existing one. Often I even add a CI/CD task that runs ESLint in the pipeline to be sure the project is error-safe and follows the configured format.

## Customize eslint ruleset

You can configure each integration individually, for example:

```js
// eslint.config.js
import antfu from '@antfu/eslint-config'

export default antfu({
  // Type of the project. 'lib' for libraries, the default is 'app'
  type: 'lib',

  // `.eslintignore` is no longer supported in Flat config, use `ignores` instead
  // The `ignores` option in the option (first argument) is specifically treated to always be global ignores
  // And will **extend** the config's default ignores, not override them
  // You can also pass a function to modify the default ignores
  ignores: [
    '**/fixtures',
    // ...globs
  ],

  // Parse the `.gitignore` file to get the ignores, on by default
  gitignore: true,

  // Enable stylistic formatting rules
  stylistic: true,

  // Or customize the stylistic rules
  stylistic: {
    indent: 2, // 4, or 'tab'
    quotes: 'single', // or 'double'
  },

  // TypeScript and Vue are autodetected, you can also explicitly enable them:
  typescript: true,
  vue: true,

  // Disable jsonc and yaml support
  jsonc: false,
  yaml: false,
})
```

For more customization see <https://github.com/antfu/eslint-config>

## Conclusion

Since I found the ESLint config from @antfu, I can set up ESLint for any project within 5 minutes and can focus on other development tasks. Meanwhile, other developers of the project can already work with the defined config.\
\
I am using the config from @antfu for any project size. From one of my private projects, a new greenfield project or existing project.\
\
The highly customizable ruleset is optimal for existing projects. As an example, it's possible to set all rule levels to warning to be able to deploy with ESLint config even when there are many ESLint errors in the code. With this, the developer can clean up the project step by step.
