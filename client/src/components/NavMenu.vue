<template>
    <div class="top-0 w-full flex justify-content-around ">
      <TabMenu :model="items" class=""/>
      <Button icon="pi pi-sign-out" class="p-button-secondary align-self-end" @click="logout()" />
    </div>
  </template>

<script setup>
import TabMenu from 'primevue/tabmenu';
import Button from 'primevue/button';
import { useRouter } from 'vue-router';
import { ref } from 'vue';

const items = ref([
  {label: 'Menu', to: '/'},
  {label: 'Cart', to: '/cart'},
  {label: 'Orders', to: '/orders'},
  {label: 'My Reviews', to: '/reviews'},
  {label: 'Messages', to: '/messages'}  
]);

const router = useRouter();

function logout() {
  sessionStorage.removeItem("token");
  sessionStorage.removeItem("cart");
  router.push("/login");
}

</script>