import {createRouter, createWebHistory} from 'vue-router'
import HomeView from "@/views/HomeView.vue";
import DashboardView from "@/views/DashboardView.vue";
import ApiSyncView from "@/views/ApiSyncView.vue";
import InterventionsView from "@/views/InterventionsView.vue";

export const paths = {
  home: '/',
  dashboard: '/dashboard',
  apiSync: 'api-sync',
  interventions: 'interventions'
}

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: HomeView
    },
    {
      path: '/dashboard',
      component: DashboardView
    },
    {
      path: '/api-sync',
      component: ApiSyncView
    },
    {
      path: '/interventions',
      component: InterventionsView
    }
  ]
})

export default router
