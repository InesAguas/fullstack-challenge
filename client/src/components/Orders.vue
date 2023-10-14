
<template>
    <div v-for="(order, i) in orders">
        <div class="card xl:flex xl:justify-content-center">
            <OrderList v-model="orders[i].plates" listStyle="height:auto" dataKey="i">
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
                    </div>
                </template>
            </OrderList>
        </div>
    </div>
</template>

<script setup>
import OrderList from 'primevue/orderlist';
import { ref, onMounted, computed } from 'vue';

const orders = ref(null);
const plates = ref();

onMounted(async () => {
    // fetch plates from server
    const URL = "https://localhost:8443/api/plates"
    const response = await fetch(URL);
    const data = await response.json();
    plates.value = data;

    // fetch orders from server
    const URL_ORDERS = "https://localhost:8443/api/orders"
    const response_orders = await fetch(URL_ORDERS);
    const data_orders = await response_orders.json();
    orders.value = data_orders;
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

</script>