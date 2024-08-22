import { createFileRoute, redirect } from '@tanstack/react-router'
import InterventionPage from '../components/pages/InterventionPage'

export const Route = createFileRoute('/intervention')({
    component: () => <div>
        <InterventionPage></InterventionPage>
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

