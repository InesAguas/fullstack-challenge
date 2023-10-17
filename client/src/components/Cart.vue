
<template>
    <NavMenu/>
    <DataTable :value="cart" tableStyle="min-width: 50rem">
        <Column field="plate_name" header="Name"></Column>
        <Column header="Picture">
            <template #body="slotProps">
                <img :src="slotProps.data.picture" :alt="slotProps.data.picture" class="w-6rem shadow-2 border-round" />
            </template>
        </Column>
        <Column field="price" header="Price"></Column>
        <Column field="quantity" header="Quantity"></Column>
        <Column header="Total">
            <template #body="slotProps">
                {{slotProps.data.price * slotProps.data.quantity}} €
            </template>
        </Column>
        <template #footer> 
            Total: {{total}} €
            <Button label="Checkout" class="p-button-success" @click="checkoutOrder()" />
        </template>
    </DataTable>
</template>

<script setup>
import NavMenu from './NavMenu.vue';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';
import { ref, onMounted, computed } from 'vue';

const cart = ref([]);
const total = ref(0);

console.log(JSON.parse(sessionStorage.getItem("cart")));
onMounted(async () => {
    cart.value = JSON.parse(sessionStorage.getItem("cart")) || [];
    cart.value.forEach(item => {
        total.value += item.price * item.quantity;
    });
});

async function checkoutOrder() {

    if(cart.value.length === 0) {
        alert("Cart is empty");
        return;
    }
  
    const URL = "https://localhost:8443/api/orders"
    const response = await fetch(URL,{
        method: "POST",
        body: JSON.stringify({
            plates: cart.value
        }),
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + sessionStorage.getItem("token")
        }
    });
    
    if(response.status === 200) {
    alert("Order placed successfully");
    sessionStorage.removeItem("cart");
    cart.value = [];
    } else {
        alert("Order failed");
    }
}

</script>