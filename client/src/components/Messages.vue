<template>
    <NavMenu/>
    <div class="card">
        <div class="flex flex-column w-12 h-30rem">
            <div class="flex flex-column bg-white h-full mb-3 overflow-y-scroll border-round-md">
                <!---MESSAGE CONTAINER-->
                <div v-for="(msg, i) in messages" :key="i" >
                    <div v-if="msg.type === 'received'" class="flex justify-content-start">
                        <div  class="m-2 px-3 py-1 border-round-lg bg-gray-300 text-black-alpha-90 max-w-20rem overflow-visible text-sm text-left" style="word-wrap: break-word;">
                            {{msg.content}}
                        </div>
                    </div>
                    <div v-else class="flex justify-content-end">
                        <div  class="m-2 px-3 py-1 border-round-lg bg-blue-400 text-black-alpha-90 max-w-20rem text-sm text-right" style="word-wrap: break-word;">
                            {{msg.content}}
                        </div>
                        
                    </div>
                </div>
            </div>
            <div class="flex">
                <InputText type="text" v-model="message" class="w-full mr-3" />
                <Button icon="pi pi-send" @click="sendMessage()"/>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';

import NavMenu from './NavMenu.vue';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';

const messages = ref([]);
const message = ref('');

const socket = new WebSocket("ws://localhost:8000/api/ws");

socket.onmessage = function(event) {
    messages.value.push({ content: event.data, type: 'received' });
    console.log(messages.value)
};

onMounted(async () => {
    
});

function sendMessage() {
    if(message.value === ''){
        return;
    } 
    messages.value.push({ content: message.value, type: 'sent' });
    socket.send(message.value);
    message.value = '';
    console.log(messages.value)
}

</script>