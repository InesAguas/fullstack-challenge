
<template>
    <div class="card">
        <DataView :value="plates" :layout="layout">
            <template #header>
                <div class="flex justify-content-end">
                    <DataViewLayoutOptions v-model="layout" />
                </div>
            </template>

            <template #list="slotProps">
                <div class="col-12">
                    <div class="flex flex-column xl:flex-row xl:align-items-start p-4 gap-4">
                        <img class="w-9 sm:w-16rem xl:w-10rem shadow-2 block xl:block mx-auto border-round" :src="slotProps.data.picture" :alt="slotProps.data.plate_name" />
                        <div class="flex flex-column sm:flex-row justify-content-between align-items-center xl:align-items-start flex-1 gap-4">
                            <div class="flex flex-column align-items-center sm:align-items-start gap-3">
                                <div class="text-2xl font-bold text-900">{{ slotProps.data.plate_name }}</div>
                            </div>
                            <div class="flex sm:flex-column align-items-center sm:align-items-end gap-3 sm:gap-2">
                                <span class="text-2xl font-semibold">{{ slotProps.data.price }} € </span>
                                <Button icon="pi pi-shopping-cart" rounded></Button>
                            </div>
                        </div>
                    </div>
                </div>
            </template>

            <template #grid="slotProps">
                <div class="col-12 sm:col-6 lg:col-12 xl:col-4 p-2">
                    <div class="p-4 border-1 surface-border surface-card border-round">
                        <div class="flex flex-column align-items-center gap-3 py-5">
                            <img class="w-9 shadow-2 border-round" :src="slotProps.data.picture" :alt="slotProps.data.plate_name" />
                            <div class="text-2xl font-bold">{{ slotProps.data.plate_name }}</div>
                        </div>
                        <div class="flex align-items-center justify-content-between">
                            <span class="text-2xl font-semibold">{{ slotProps.data.price }} €</span>
                            <Button icon="pi pi-shopping-cart" rounded></Button>
                        </div>
                    </div>
                </div>
            </template>
        </DataView>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import Button from 'primevue/button';

import DataView from 'primevue/dataview';
import DataViewLayoutOptions from 'primevue/dataviewlayoutoptions'   // optional

const plates = ref();
const layout = ref('grid');

onMounted(async () => {
    // fetch data from server
    const URL = "https://localhost:8443/api/plates"
    const response = await fetch(URL);
    const data = await response.json();
    plates.value = data;
});

</script>
