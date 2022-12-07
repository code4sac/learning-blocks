import {createRouter, createWebHistory} from 'vue-router'
// import {log} from '@/lib/logging'

const router = createRouter({
    // history: createWebHistory(import.meta.env.BASE_URL),
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'home',
            component: () => import('@/views/ReportCardHome.vue'),
        },
        {
            path: '/report',
            name: 'report',
            component: () => import('@/views/ReportCardDetail.vue'),
        }]
})

// router.onError((error) => {
//     log.error(`Error in router: ${error}`)
// })

export default router