
<template>
    <NavMenu/>
    <div v-for="(order, i) in orders" :key="i">
        <div class="card xl:flex xl:justify-content-center">
            <OrderList v-model="orders[i].plates" listStyle="height:auto" dataKey="plate_id">
                <template #header>
                    <div class="flex gap-5">
                        <span># {{ orders[i].order_id }}</span>
                        <span>{{ parseTimeToString(orders[i].order_time) }}</span>
                        <span>Total: {{ getOrderTotal(orders[i].order_id) }} €</span>
                    </div>
                    
                </template>
                <template #item="slotProps">
                    <div class="flex flex-wrap p-2 align-items-center gap-3">
                        <img class="w-4rem shadow-2 flex-shrink-0 border-round" :src="plateImage(slotProps.item.plate_id)" :alt="slotProps.item.name" />
                        <div class="flex-1 flex flex-column gap-2">
                            <span class="font-bold w-10rem">{{ slotProps.item.quantity }} x {{ slotProps.item.plate_name }}</span>
                        </div>
                        <span class="font-bold text-900">{{ platePrice(slotProps.item.plate_id) * slotProps.item.quantity }} €</span>
                        <Button label="Review Item" :disabled="plateReview(slotProps.item.plate_id)" @click="selectedPlate = slotProps.item, visible = true"/>

                    </div>
                </template>
            </OrderList>
        </div>
        <div>
            <Button label="Order Again" />
        </div>
        <Dialog v-if="selectedPlate" v-model:visible="visible" modal :header="selectedPlate.plate_name" :style="{ width: '50vw' }">
            <div class="card">
                <Rating v-model="rating" :cancel="false" :stars="5" />
                <Textarea v-model="comment" rows="5" cols="30" />
            </div>
            <template #footer>
                <Button label="Submit" icon="pi pi-check" @click="submitReview()"/>
            </template>
        </Dialog>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';

import OrderList from 'primevue/orderlist';
import NavMenu from './NavMenu.vue';
import Button from 'primevue/button';
import Dialog from 'primevue/dialog';
import Rating from 'primevue/rating';
import Textarea from 'primevue/textarea';


const orders = ref(null);
const plates = ref();
const reviews = ref([]);
const visible = ref(false);
const selectedPlate = ref(null);

const rating = ref(0);
const comment = ref('');

onMounted(async () => {
    // fetch plates from server
    const URL = "https://localhost:8443/api/plates"
    const response = await fetch(URL, {
        headers: {
            "Authorization": "Bearer " + sessionStorage.getItem("token")
        }
    });
    const data = await response.json();
    plates.value = data;

    // fetch orders from server
    const URL_ORDERS = "https://localhost:8443/api/orders"
    const response_orders = await fetch(URL_ORDERS, {
        headers: {
            "Authorization": "Bearer " + sessionStorage.getItem("token")
        }
    });
    const data_orders = await response_orders.json();
    orders.value = data_orders;

    //fetch user reviews
    const URL_REVIEWS = "https://localhost:8443/api/reviews"
    const response_reviews = await fetch(URL_REVIEWS, {
        headers: {
            "Authorization": "Bearer " + sessionStorage.getItem("token")
        }
    });

    const data_reviews = await response_reviews.json();
    reviews.value = data_reviews;
    
});


function platePrice(itemId) {
    return plates.value.find(plate => plate.plate_id === itemId).price
}

function plateImage(itemId) {
    return plates.value.find(plate => plate.plate_id === itemId).picture
}

function parseTimeToString(timestamp) {
    const regex = /(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2})/;
    let matches = timestamp.match(regex);
    if (matches) {
        return matches[1] + " " + matches[2];
    }
}

function getOrderTotal(orderId) {
    let total = 0;
    orders.value.find(order => order.order_id === orderId).plates.forEach(plate => {
        total += platePrice(plate.plate_id) * plate.quantity;
    });
    return total.toFixed(2);
}

function plateReview(itemId) {
    return reviews.value.find(review => review.plate_id === itemId);
}

async function submitReview() {
    if(rating.value === 0) {
        alert("Please select a rating");
        return;
    }

    console.log(selectedPlate.value.plate_id)
    console.log(rating.value)
    console.log(comment.value)

    const URL = "https://localhost:8443/api/reviews"
    const response = await fetch(URL,{
        method: "POST",
        body: JSON.stringify({
            plate_id: selectedPlate.value.plate_id,
            rating: rating.value,
            comment: comment.value
        }),
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + sessionStorage.getItem("token")
        }
    });


    if(response.status === 200) {
        alert("Review submitted successfully");
        reviews.value.push( await response.json());
        rating.value = 0;
        comment.value = '';
        visible.value = false;
    } else {
        alert("Review failed");
    }
}

</script>