<template>
    <CreatePost/>
    <div class="flex flex-col gap-4 mb-8">
        <FeedPost
            v-for="publication in store.publications"
            :key="publication.id"
            :publication="publication"
        />
    </div>
</template>

<script setup lang="ts">
import { usePublicationsStore } from '~/store/publications';

const store = usePublicationsStore();

onMounted(async () => {
    await store.loadData();
    console.log(JSON.stringify(store.publications, null, 2));
});
</script>

<style scoped>

</style>