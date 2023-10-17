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
  {label: 'Cart', to: '/cart'},
  {label: 'Orders', to: '/orders'},
  {label: 'My Reviews', to: '/reviews'}
]);

</script>