<template>
    <div class="card">
        <div class="field">
    <span class="p-float-label">
        <InputText id="email" v-model="email"/>
        <label for="email">Email</label>
    </span>
    </div>
    <div class="field">
    <span class="p-float-label">
        <Password v-model="password" :feedback="false" toggleMask />
        <label for="password">Password</label>
    </span>
</div>

    <Button label="Login" />
</div>
    
</template>

<script setup>
import { ref, onMounted } from 'vue';

import InputText from 'primevue/inputtext';
import Password from 'primevue/password';
import Button from 'primevue/button';

const email = ref('');
const password = ref('');
</script>