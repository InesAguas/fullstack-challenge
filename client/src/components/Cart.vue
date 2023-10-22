
<template>
    <NavMenu/>
    <div class="card">
    <DataTable :value="cart"  tableStyle="min-width: 10rem">
        <Column field="plate_name" header="Name"></Column>
        <Column header="Picture">
            <template #body="slotProps">
                <img :src="slotProps.data.picture" :alt="slotProps.data.picture" class="w-6rem shadow-2 border-round" />
            </template>
        </Column>
        <Column header="Price">
            <template #body="slotProps">
                {{slotProps.data.price}} €
            </template>
        </Column>
        <Column header="Quantity">
            <template #body="slotProps">
                <InputNumber v-model="slotProps.data.quantity" showButtons buttonLayout="vertical" style="width: 3rem"
    decrementButtonClassName="p-button-secondary" incrementButtonClassName="p-button-secondary" incrementButtonIcon="pi pi-plus" decrementButtonIcon="pi pi-minus" :min="1" :max="20"/>
        </template>
        </Column>
        <Column header="Total">
            <template #body="slotProps">
                {{(slotProps.data.price * slotProps.data.quantity).toFixed(2)}} €
            </template>
        </Column>
        <Column header="Actions">
            <template #body="slotProps">
                <Button icon="pi pi-trash" severity="danger" text rounded outlined raised aria-label="Cancel" @click="removeItem(slotProps.data.plate_id)"/>
            </template>
        </Column>
        <template #footer> 
            <div class="flex justify-content-between">
                <p>Total: {{total}} €</p>
                <Button label="Checkout"  severity="success" @click="checkoutOrder()" raised size="small" :disabled="total<=0"/>
            </div>
        </template>
    </DataTable>
    <Message v-if="success" severity="success" :sticky="false">Order placed successfully!</Message>
</div>
<Toast position="bottom-left"/>

</template>

<script setup>
import NavMenu from './NavMenu.vue';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';
import InputNumber from 'primevue/inputnumber';
import Message from 'primevue/message';

import Toast from 'primevue/toast';

import { useToast } from "primevue/usetoast";
const toast = useToast();

import { ref, onMounted, computed, watch } from 'vue';

const cart = ref([]);
const total = ref(0);
const success = ref(false);


onMounted(async () => {
    cart.value = JSON.parse(sessionStorage.getItem("cart")) || [];
    calculateTotal();
});

watch(cart, (newValue, oldValue) => {
    sessionStorage.setItem("cart", JSON.stringify(newValue));
    calculateTotal();
}, {deep: true});

function calculateTotal() {
    let newTotal = 0;
    cart.value.forEach(item => {
        newTotal += item.price * item.quantity;
    });

    total.value = newTotal.toFixed(2);
}

async function checkoutOrder() {
    

    if(cart.value.length === 0) {
        displayToast("error", "Cart is empty!");
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
        success.value = true;
        sessionStorage.removeItem("cart");
        cart.value = [];
        total.value = 0;
    }
}

const displayToast = (severity, message) => {
    toast.add({ severity: severity, summary: 'Info', detail: message, life: 3000 });
};

function removeItem(plateId) {
    const index = cart.value.findIndex(item => item.plate_id === plateId);
    cart.value.splice(index, 1);
    displayToast("success", "Item removed from cart!");
}

</script>