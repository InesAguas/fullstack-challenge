<script setup>
import TabMenu from 'primevue/tabmenu';
import { ref } from 'vue';

const items = ref([
  {label: 'Menu', to: '/'},
  {label: 'Orders', to: '/orders'},
]);

</script>

<template>
  <div class="top-0">
    <TabMenu :model="items" />
    <router-view />
  </div>
</template>

<style scoped>

</style>
