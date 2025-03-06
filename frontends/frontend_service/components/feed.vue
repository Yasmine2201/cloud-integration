<template>
    <CreatePost/>
    <pre>{{ loadedPubs}}</pre>
</template>

<script setup lang="ts">
import { usePublicationsStore } from '~/store/publications';

const store = usePublicationsStore();

onMounted(async () => {
    await store.loadData();
});

const loadedPubs = computed(() => {
    return store.publications ? JSON.stringify(store.publications, null, 2) : store.publications
});
</script>

<style scoped>

</style>