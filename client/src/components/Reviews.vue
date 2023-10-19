
<template>
    <NavMenu/>
    <div class="card">
        <DataTable :value="reviews"   paginator :rows="4" :rowsPerPageOptions="[4, 6, 8, 10]" tableStyle="max-width: 50rem;" >
            <Column header="Plate Name">
                <template #body="slotProps">
                  {{ plateName(slotProps.data.plate_id) }}
                 </template>
            </Column>
            <Column header="Picture">
                <template #body="slotProps">
                <img :src="plateImage(slotProps.data.plate_id)" class="w-6rem shadow-2 border-round" />
            </template>
            </Column>
            <Column header="Rating">
                <template #body="slotProps">
                    <Rating v-model="slotProps.data.rating" :cancel="false" readonly />
                </template>
            </Column>
            <Column  header="Comment" >
                <template #body="slotProps">
                    <p class="sm:max-w-10rem md:max-w-20rem" style="word-wrap: break-word">{{ slotProps.data.comment }}</p>
                </template>
            </Column>
        </DataTable>
</div>
</template>

<script setup>
import NavMenu from './NavMenu.vue';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Rating from 'primevue/rating';
import { ref, onMounted, computed } from 'vue';

const reviews = ref([]);
const plates = ref();

onMounted(async () => {
    const URL_PLATES = "https://localhost:8443/api/plates"
    const response_plates = await fetch(URL_PLATES)
    const data_plates = await response_plates.json();
    plates.value = data_plates;

    const URL = "https://localhost:8443/api/reviews"
    const response = await fetch(URL, {
        headers: {
            "Authorization": "Bearer " + sessionStorage.getItem("token")
        }
    });
    const data = await response.json();
    reviews.value = data;   
});

function plateName(plateId) {
    return plates.value.find(plate => plate.plate_id === plateId).plate_name;
}

function plateImage(plateId) {
    return plates.value.find(plate => plate.plate_id === plateId).picture;
}

</script>