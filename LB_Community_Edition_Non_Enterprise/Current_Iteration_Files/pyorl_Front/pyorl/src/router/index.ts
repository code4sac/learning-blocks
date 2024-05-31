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
      name: 'Dashboard',
      component: DashboardView
    },
    {
      path: '/api-sync',
      name: 'API Sync',
      component: ApiSyncView
    },
    {
      path: '/interventions',
      name: 'Interventions',
      component: InterventionsView
    }
  ]
})

/**
 * Set the title of the page based on the current route.
 * Home: Learning Blocks
 * Another Route: Learning Blocks - Another Route
 */
router.beforeEach((to, from, next) => {
  document.title = `Learning Blocks${to.name ? ' - ' + to.name : ''}`;
  next();
});

export default router
