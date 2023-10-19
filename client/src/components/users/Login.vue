<template>
    <div class="flex flex-wrap card w-20rem justify-content-center" >
        <h2 class="w-15rem mt-0 uppercase">Login</h2>
        <div>
            <span class="p-float-label">
                <InputText id="username" v-model="username" class="w-15rem" />
                <label for="username">Username</label>
            </span>
        </div>
        <div>
            <span class="p-float-label mt-5">
                <Password v-model="password" :feedback="false"  toggleMask />
                <label for="password">Password</label>
            </span>
        </div>
        <p class="text-sm">Don't have an account yet? <router-link to="/registration">Sign up</router-link></p>
        <Button label="Login" @click="login()" class="mt-2 w-9" />
        <Message v-if="failed" severity="error" >{{message}}</Message>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

import InputText from 'primevue/inputtext';
import Password from 'primevue/password';
import Button from 'primevue/button';
import Message from 'primevue/message';

const username = ref('');
const password = ref('');
const failed = ref(false);
const message = ref('');
const router = useRouter();


async function login() {
    if(username.value === ''){
        message.value = "Username cannot be empty";
        failed.value = true;
        return;
    }

    if(password.value === '') {
        message.value = "Password cannot be empty";
        failed.value = true;
        return;
    }

    const URL = "https://localhost:8443/api/users/login"
    const response = await fetch(URL, {
        method: "POST",
        body: JSON.stringify({
            username: username.value,
            password: password.value
        }),
        headers: {
            "Content-Type": "application/json"
        }
    });

    if (response.status === 200) {
        const data = await response.json();
        sessionStorage.setItem("token", data.token);
        router.push("/");

    } else {
        let data = await response.json();
        message.value = data.details;
        failed.value = true;
    }

}

</script>