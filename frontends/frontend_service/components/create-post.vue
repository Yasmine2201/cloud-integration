<template>
  <div class="p-4">
    <UCard class="block">
    <button @click="isModalOpen = true" class="w-full text-start">
        <p class="hover:bg-red-100 rounded-full px-4 py-2 border-red-300 border font-sans text-red-950 transition-all">Commencer un post</p>
    
    </button></UCard>

    <UModal v-model="isModalOpen">
      <UCard>
        <UInput
          placeholder="Un petit mot doux ?"
          v-model="postTitle"
          input-class="text-xl font-semibold"
          color="primary"
          variant="none"
        />
        <UTextarea
          v-model="postBody"
          placeholder="J'adore les chats roux."
          :rows="10"
          color="primary"
          variant="none"
          autoresize
        />
        <div class="flex justify-end">
          <UButton :disabled="!canSend" :color="canSend ? 'primary' : 'gray'" @click="sendPost">
            Envoyer
          </UButton>
        </div>
      </UCard>
    </UModal>
  </div>
</template>
<script setup lang="ts">
import { usePublicationsStore } from '~/store/publications';

const isModalOpen = ref<boolean>(false);
const postTitle = ref<string>("");
const postBody = ref<string>("");
const canSend = computed(() => Boolean(postTitle.value && postBody.value));
const store = usePublicationsStore();

async function sendPost() {
    await store.createPublication({
        title: postTitle.value,
        body: postBody.value
    });
    isModalOpen.value = false;
}

</script>
<style></style>
