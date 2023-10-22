<template>
    <div class="flex flex-wrap card w-20rem justify-content-center" >
        <h2 class="w-15rem mt-0 uppercase">Sign Up</h2>
        <div class="flex flex-column">
            <label for="username" class="align-self-start">Username</label>
            <InputText id="username" v-model="username" class="w-15rem" />

        </div>
        <div class="flex flex-column mt-2">
            <label for="password" class="align-self-start">Password</label>
            <Password v-model="password"  toggleMask >  
                <template #footer>
                    <Divider />
                    <p class="mt-2">Must have:</p>
                    <ul class="pl-2 ml-2 mt-0" style="line-height: 1.5">
                        <li>At least one lowercase</li>
                        <li>At least one uppercase</li>
                        <li>At least one number</li>
                        <li>Minimum 8 characters</li>
                    </ul>
                </template>
            </Password>
        </div>
        <p class="text-sm">Already have an account? <router-link to="/login">Sign in</router-link></p>
        <Button label="Sign up" @click="signUp()" class="mt-2 w-9" />

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

import Divider from 'primevue/divider';

const username = ref('');
const password = ref('');

const message = ref('');
const failed = ref(false);

const router = useRouter();

async function signUp() {

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

    const URL = "https://localhost:8443/api/users/registration"
    const response = await fetch(URL, {
        method: "POST",
        body: JSON.stringify({
            username: username.value.toLowerCase(),
            password: password.value
        }),
        headers: {
            "Content-Type": "application/json"
        }
    });

    if (response.status === 200) {
        router.push("/login");
    } else {
        let data = await response.json();
        message.value = data.detail;
        failed.value = true;
    }
}
</script>