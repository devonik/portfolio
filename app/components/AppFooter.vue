<script setup lang="ts">
const { footer } = useAppConfig()
</script>

<template>
  <UFooter
    class="z-10 bg-default"
    :ui="{ left: 'text-muted text-xs' }"
  >
    <template #left>
      <div class="flex flex-col gap-1 sm:flex-row sm:items-center sm:gap-3">
        <span>{{ footer.credits }}</span>
        <div class="flex items-center gap-3">
          <ULink
            to="/imprint"
            class="hover:text-default"
          >
            Imprint
          </ULink>
          <ULink
            to="/privacy"
            class="hover:text-default"
          >
            Privacy
          </ULink>
          <ULink
            to="/legal"
            class="hover:text-default"
          >
            Legal
          </ULink>
        </div>
      </div>
    </template>

    <template #right>
      <template v-if="footer?.links">
        <UButton
          v-for="(link, index) of footer?.links"
          :key="index"
          v-bind="{ size: 'xs', color: 'neutral', variant: 'ghost', ...link }"
        />
      </template>
    </template>
  </UFooter>
</template>
