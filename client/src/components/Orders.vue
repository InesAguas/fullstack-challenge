
<template>
    <NavMenu />

    <div class="card">
        <DataTable :value="orders" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20]" dataKey="order_id"
            v-model:expandedRows="expandedRows" tableStyle="min-width: 60rem">
            <Column expander style="width: 5rem" />
            <Column header="Order Number">
                <template #body="slotProps">
                    #{{ slotProps.data.order_id }}
                </template>
            </Column>
            <Column header="Date Ordered">
                <template #body="slotProps">
                    {{ parseTimeToString(slotProps.data.order_time) }}
                </template>
            </Column>
            <Column header="Status">
                <template #body="slotProps">
                    <Tag :severity="tagColor(slotProps.data.order_status)" :value="slotProps.data.order_status"></Tag>
                </template>
            </Column>
            <Column header="Update Order Status">
                <template #body="slotProps">

                    <div class="flex flex-wrap justify-content-between"
                        v-if="slotProps.data.order_status != 'Rejected' && slotProps.data.order_status != 'Canceled' && slotProps.data.order_status != 'Delivered'">
                        <div class="flex flex-column gap-2 align-self-center">
                            <div class="flex align-items-center" v-if="slotProps.data.order_status === 'Submitted'">
                                <RadioButton v-model="slotProps.data.next_order_state" inputId="1" name="status"
                                    value="Approved" />
                                <label for="1" class="ml-2 text-sm">Approved</label>
                            </div>
                            <div class="flex align-items-center" v-if="slotProps.data.order_status === 'Submitted'">
                                <RadioButton v-model="slotProps.data.next_order_state" inputId="2" name="status"
                                    value="Rejected" size="small" />
                                <label for="2" class="ml-2 text-sm">Rejected</label>
                            </div>
                            <div class="flex align-items-center" v-if="slotProps.data.order_status === 'Approved'">
                                <RadioButton v-model="slotProps.data.next_order_state" disabled inputId="3" name="status"
                                    value="In Preparation" size="small" />
                                <label for="2" class="ml-2 text-sm">In Preparation</label>
                            </div>
                            <div class="flex align-items-center" v-if="slotProps.data.order_status === 'In Preparation'">
                                <RadioButton v-model="slotProps.data.next_order_state" disabled inputId="4" name="status"
                                    value="In Delivery" size="small" />
                                <label for="2" class="ml-2 text-sm">In Delivery</label>
                            </div>
                            <div class="flex align-items-center" v-if="slotProps.data.order_status === 'In Delivery'">
                                <RadioButton v-model="slotProps.data.next_order_state" disabled inputId="5" name="status"
                                    value="Delivered" size="small" />
                                <label for="2" class="ml-2 text-sm">Delivered</label>
                            </div>
                        </div>
                        <Button label="Update Status" class="p-button-success p-1 mb-2 text-xs" size="small"
                            title="Update Order Status" @click="updateOrderStatus(slotProps.data.order_id)" />
                    </div>
                    <div class="flex justify-content-end">
                        <Button v-if="canOrderBeCancelled(slotProps.data.order_status)"
                            @click="slotProps.data.next_order_state = 'Canceled', updateOrderStatus(slotProps.data.order_id)"
                            label="Cancel Order" class="p-button-danger text-xs p-1 align-self-end " size="small"
                            title="Cancel Order" />
                    </div>

                </template>
            </Column>

            <template #expansion="slotProps">
                <div class="mx-6 flex flex-column align-content-center">
                    <OrderList v-model="slotProps.data.plates" listStyle="height:auto" dataKey="plate_id">
                        <template #header>
                            <div class="flex gap-5">
                                <span>Total: {{ getOrderTotal(slotProps.data.order_id) }} €</span>
                            </div>
                        </template>
                        <template #item="innerSlotProps">
                            <div class="flex flex-wrap p-2 align-items-center gap-3">
                                <img class="w-4rem shadow-2 flex-shrink-0 border-round"
                                    :src="plateImage(innerSlotProps.item.plate_id)" :alt="innerSlotProps.item.name" />
                                <div class="flex-1 flex flex-column gap-2">
                                    <span class="font-bold w-10rem">{{ innerSlotProps.item.quantity }} x {{
                                        innerSlotProps.item.plate_name }}</span>
                                </div>
                                <span class="font-bold text-900">{{ platePrice(innerSlotProps.item.plate_id) *
                                    innerSlotProps.item.quantity }} €</span>
                                <div class="w-9rem">
                                <Button v-if="slotProps.data.order_status === 'Delivered' && !plateReview(innerSlotProps.item.plate_id)" label="Review Item" 
                                    @click="selectedPlate = innerSlotProps.item, rating = 0, comment = '', visible = true" />
                                </div>
                            </div>
                        </template>

                    </OrderList>
                </div>
            </template>
        </DataTable>
    </div>
    <Dialog v-if="selectedPlate" v-model:visible="visible" modal
        :header="selectedPlate.plate_name + ' - ' + platePrice(selectedPlate.plate_id) + '€'" :style="{ width: '50vw' }">
        <div class="flex flex-column">
            <img class="sm:w-5 md:w-3 shadow-2 border-round" :src="plateImage(selectedPlate.plate_id)"
                :alt="selectedPlate.plate_name" />
            <div class="flex gap-3">
                <p>Your Rating: </p>
                <Rating v-model="rating" :cancel="false" :stars="5" />
            </div>
            <label for="comment">Comments:</label>
            <Textarea v-model="comment" rows="5" cols="30" />
        </div>
        <Message v-if="failed" severity="error" >{{message}}</Message>
        <template #footer>
            <Button label="Submit" icon="pi pi-check" @click="submitReview()" />
        </template>
    </Dialog>

    <Toast position="bottom-left"/>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';

import OrderList from 'primevue/orderlist';
import NavMenu from './NavMenu.vue';
import Button from 'primevue/button';
import Dialog from 'primevue/dialog';
import Rating from 'primevue/rating';
import Textarea from 'primevue/textarea';
import Tag from 'primevue/tag';
import Column from 'primevue/column';
import DataTable from 'primevue/datatable';
import RadioButton from 'primevue/radiobutton';
import Toast from 'primevue/toast';
import Message from 'primevue/message';

import { useToast } from "primevue/usetoast";
const toast = useToast();


const orders = ref(null);
const plates = ref();
const reviews = ref([]);
const visible = ref(false);
const selectedPlate = ref(null);
const expandedRows = ref([]);


const rating = ref(0);
const comment = ref('');

const failed = ref(false);
const message = ref('');


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

    defaultNextOrderState();

});


function defaultNextOrderState() {
    orders.value.forEach(order => {
        switch (order.order_status) {
            case "Submitted":
                order.next_order_state = "Approved";
                break;
            case "Approved":
                order.next_order_state = "In Preparation";
                break;
            case "In Preparation":
                order.next_order_state = "In Delivery";
                break;
            default:
                order.next_order_state = "Delivered";
        }
    });
}

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

function canOrderBeCancelled(status) {
    return status === "Submitted" || status === "Approved";
}

function tagColor(status) {
    if (status === "Delivered") {
        return "success";
    } else if (status === "Canceled" || status === "Rejected") {
        return "danger";
    } else {
        return "warning";
    }
}

async function submitReview() {
    if (rating.value === 0) {
        message.value = "Please select a rating";
        failed.value = true;
        return;
    }

    const URL = "https://localhost:8443/api/reviews"
    const response = await fetch(URL, {
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


    if (response.status === 200) {
        reviews.value.push(await response.json());
        visible.value = false;
        displayToast('success', "Review submitted successfully");
    } else {
       message.value = "Review submission failed";
       failed.value = true;
    }


}

async function updateOrderStatus(orderId) {
    const URL = "https://localhost:8443/api/orders/status/" + orderId
    let index = orders.value.findIndex(order => order.order_id === orderId);
    const response = await fetch(URL, {
        method: "PUT",
        body: JSON.stringify({
            order_status: orders.value[index].next_order_state
        }),
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + sessionStorage.getItem("token")
        }
    });

    if (response.status === 200) {
        displayToast('success', "Order status updated successfully");
        orders.value[index].order_status = orders.value[index].next_order_state;
        defaultNextOrderState();
    } else {
        displayToast('error', "Order status update failed");
    }

}

const displayToast = (severity, message) => {
    toast.add({ severity: severity, summary: 'Info', detail: message, life: 3000 });
};

</script>