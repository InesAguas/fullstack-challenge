<template>
    <div class="card">
        <div class="field">
    <span class="p-float-label">
        <InputText id="username" v-model="username"/>
        <label for="username">Username</label>
    </span>
    </div>
    <div class="field">
    <span class="p-float-label">
        <Password v-model="password" :feedback="false" toggleMask />
        <label for="password">Password</label>
    </span>
</div>
    <Button label="Login" @click="login()"/>
</div>
    
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

import InputText from 'primevue/inputtext';
import Password from 'primevue/password';
import Button from 'primevue/button';

const username = ref('');
const password = ref('');
const router = useRouter();


async function login() {
    const URL = "https://localhost:8443/api/users/login"
    const response = await fetch(URL,{
        method: "POST",
        body: JSON.stringify({
            username: username.value,
            password: password.value
        }),
        headers: {
            "Content-Type": "application/json"
        }
    });
    
    if(response.status === 200) {
        const data = response.json();
        sessionStorage.setItem("token", data.token);
        router.push("/");
        
    } else {
        alert("Login failed");
    }
}

</script>