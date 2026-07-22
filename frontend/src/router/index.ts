import { createRouter, createWebHistory } from 'vue-router'

import CustomerQueuePage from '@/pages/CustomerQueuePage.vue'

const router = createRouter({
  history: createWebHistory(),

  routes: [
    {
      path: '/:publicCode',
      name: 'customer-queue',
      component: CustomerQueuePage,
    },
  ],
})

export default router
