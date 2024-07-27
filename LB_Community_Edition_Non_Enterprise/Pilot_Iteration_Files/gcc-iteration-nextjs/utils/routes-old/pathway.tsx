import {createFileRoute, redirect} from '@tanstack/react-router'
import PathwayPage from '../components/pages/PathwayPage'

export const Route = createFileRoute('/pathway')({
    component: () => <div>
        <PathwayPage></PathwayPage>
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

