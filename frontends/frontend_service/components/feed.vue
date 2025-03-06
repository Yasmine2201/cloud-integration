<template>
    <pre>{{ loadedPubs}}</pre>
</template>

<script setup lang="ts">
import { usePublicationsStore } from '~/store/publications';

const {loadData, publications} = usePublicationsStore();

onMounted(async () => {
    await loadData();
});

const loadedPubs = computed(() => {
    return publications ? JSON.stringify(publications, null, 2) : publications
});
</script>

<style scoped>

</style>