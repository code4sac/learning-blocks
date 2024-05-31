import {createRouter, createWebHistory} from 'vue-router'
// import {log} from '@/lib/logging'

const router = createRouter({
    // history: createWebHistory(import.meta.env.BASE_URL),
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'home',
            component: () => import('@/views/AriesApiContainer.vue'),
        },
        {
            path: '/report/:localStorageKey',
            name: 'report',
            component: () => import('@/views/ReportCardDetail.vue'),
        },
        {
            path: '/students/:localStorageKey',
            name: 'students',
            component: () => import('@/views/StudentsDetail.vue'),
        },
        {
            path: '/enrollment/:localStorageKey',
            name: 'enrollment',
            component: () => import('@/views/EnrollmentDetail.vue'),
        }
    ]

})

// router.onError((error) => {
//     log.error(`Error in router: ${error}`)
// })

export default router