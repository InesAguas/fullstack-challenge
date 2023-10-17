import { createRouter, createWebHashHistory } from 'vue-router'

import Menu from '@/components/Menu.vue'
import Orders from '@/components/Orders.vue'
import Login from '@/components/users/Login.vue'
import Registration from '@/components/users/Registration.vue'
import Cart from '@/components/Cart.vue'
import Reviews from '@/components/Reviews.vue'

// 2. Define some routes
// Each route should map to a component.
// We'll talk about nested routes later.
const routes = [
  { path: '/', component: Menu },
  { path: '/orders', component: Orders },
  { path: '/login', component: Login },
  { path: '/registration', component: Registration },
  { path: '/cart', component: Cart},
  { path: '/reviews', component: Reviews},
]

// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
const router = createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: createWebHashHistory(),
  routes, // short for `routes: routes`
})

export default router;
