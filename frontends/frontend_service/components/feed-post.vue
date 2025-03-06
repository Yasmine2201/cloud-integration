<template>
  <UCard>
    <UInput
      v-model="props.publication.title"
      input-class="text-xl font-semibold"
      color="primary"
      variant="none"
      disabled
    />
    <UTextarea
      v-model="props.publication.body"
      color="primary"
      variant="none"
      :rows="1"
      autoresize
      disabled
    />
    <div class="flex justify-end">
          
    </div>
  </UCard>
</template>
<script setup lang="ts">
import type { Publication } from '~/store/publications';

const props = defineProps<{
  publication: Publication,
}>();
</script>
<style></style>
