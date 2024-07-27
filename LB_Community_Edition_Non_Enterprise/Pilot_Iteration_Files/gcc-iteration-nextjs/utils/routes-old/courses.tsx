import {createFileRoute, redirect} from '@tanstack/react-router'
import CoursesPage from '../components/pages/CoursesPage'

export const Route = createFileRoute('/courses')({
    component: () => <div>
        <CoursesPage></CoursesPage>
    </div>,
    beforeLoad: async ({context, location}) => {
        if (!context.auth.isAuthenticated) {
            throw redirect({
                to: '/login',
                search: {
                    redirect: location.href,
                },
            })
        }
    },
    loader: ({context}) => {
        console.log(`Index: ${context.auth.user}`)
    },
})

