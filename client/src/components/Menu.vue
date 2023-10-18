
<template>
    <NavMenu/>
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
                                
                                <Button icon="pi pi-shopping-cart" rounded @click="addToCart(slotProps.data)"></Button>
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
                            <div>
                            <Button label="Reviews" link @click="selectedPlate = slotProps.data, getItemReviews(), visible = true" />
                            <Button icon="pi pi-shopping-cart" rounded @click="addToCart(slotProps.data)"></Button>
                        </div>
                        </div>
                    </div>
                </div>
            </template>
        </DataView>
    </div>
    <Dialog v-if="selectedPlate" v-model:visible="visible" modal header="Reviews" :style="{ width: '50vw' }">
         <Rating v-model="rating" :cancel="false" :stars="5" readonly/>
        <DataView :value="selectedPlateReviews">
            <template #list="slotProps">
                <div class="col-12">
                    <div>
                        {{ slotProps.data.username }}
                        <Rating v-model="slotProps.data.rating" :cancel="false" readonly />
                        {{ slotProps.data.comment }}
                    </div>
                </div>
            </template>
        </DataView>
    </Dialog>
</template>

<script setup>
import { ref, onMounted } from "vue";
import Button from 'primevue/button';

import DataView from 'primevue/dataview';
import DataViewLayoutOptions from 'primevue/dataviewlayoutoptions'   // optional

import NavMenu from './NavMenu.vue';
import Dialog from 'primevue/dialog';
import Rating from 'primevue/rating';

const plates = ref();
const layout = ref('grid');
const selectedPlate = ref();
const visible = ref(false);
const selectedPlateReviews = ref();
const rating = ref(0);

onMounted(async () => {
    // fetch data from server
    const URL = "https://localhost:8443/api/plates"
    const response = await fetch(URL);
    const data = await response.json();
    plates.value = data;
});

function addToCart(item) {
    const cart = JSON.parse(sessionStorage.getItem("cart")) || [];
    const index = cart.findIndex(cartItem => cartItem.plate_id === item.plate_id);
    if(index === -1) {
        item.quantity = 1;
        cart.push(item);
    } else {
        cart[index].quantity++;
    }
    sessionStorage.setItem("cart", JSON.stringify(cart));
    console.log(cart)
}

function calculateAverageRating() {
    let sum = 0;
    selectedPlateReviews.value.forEach(review => {
        sum += review.rating;
    });
    console.log(sum)
    return sum / selectedPlateReviews.value.length;
}

async function getItemReviews() {
    const URL = "https://localhost:8443/api/reviews/plate/" + selectedPlate.value.plate_id;
    const response = await fetch(URL);
    const data = await response.json();
    selectedPlateReviews.value = data;
    
    rating.value = calculateAverageRating();
}

</script>
