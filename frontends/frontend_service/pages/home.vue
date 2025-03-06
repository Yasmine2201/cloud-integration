<script setup lang="ts">
definePageMeta({
  middleware: "auth",
  layout: "default"
});
</script>

<template>
  <div class="max-w-xl pt-10 mx-auto">
    <Feed/>
  </div>
</template>

<style scoped>

</style>