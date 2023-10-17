
<template>
    <NavMenu/>
    <div class="card">
</div>
</template>

<script setup>
import NavMenu from './NavMenu.vue';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';
import { ref, onMounted, computed } from 'vue';

const reviews = ref([]);

onMounted(async () => {
    const URL = "https://localhost:8443/api/reviews"
    const response = await fetch(URL, {
        headers: {
            "Authorization": "Bearer " + sessionStorage.getItem("token")
        }
    });
    reviews.value = await response.json();
});

</script>