import {createFileRoute, redirect} from '@tanstack/react-router'
import StudentPage from '../components/pages/StudentPage'

export const Route = createFileRoute('/student')({
    component: () => <div>
        <StudentPage></StudentPage>
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

