<template>
  <UCard>
    <UInput
      v-model="postTitle"
      input-class="text-xl font-semibold"
      color="primary"
      variant="none"
      disabled
    />
    <UTextarea
      v-model="postBody"
      color="primary"
      variant="none"
      autoresize
    />
    <div class="flex justify-end">
          
    </div>
  </UCard>
</template>
<script setup lang="ts">
const postTitle = ref<string>("J'aime les chats roux");
const postBody = ref<string>("Whoa");
</script>
<style></style>
