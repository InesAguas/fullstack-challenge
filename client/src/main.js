import { createApp } from 'vue';
import './style.css'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config'

//theme
import "primevue/resources/themes/lara-light-indigo/theme.css";     
    
//core
import "primevue/resources/primevue.min.css";

import 'primeflex/primeflex.css';

import 'primeicons/primeicons.css';

const app = createApp(App)

app.use(router)
app.use(PrimeVue)

app.mount('#app')
