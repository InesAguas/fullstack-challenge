<template>
    <div class="top-0">
      <TabMenu :model="items" />
    </div>
  </template>

<script setup>
import TabMenu from 'primevue/tabmenu';
import { ref } from 'vue';

const items = ref([
  {label: 'Menu', to: '/'},
  {label: 'Orders', to: '/orders'},
]);

</script>