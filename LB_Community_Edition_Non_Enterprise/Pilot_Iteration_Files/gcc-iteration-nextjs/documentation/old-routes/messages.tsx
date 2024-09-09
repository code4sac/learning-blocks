import { createFileRoute, redirect } from '@tanstack/react-router'
import ContactPage from '../components/pages/MessagesPage'

export const Route = createFileRoute('/messages')({
    component: () => <div>
        <ContactPage selectedSubMenu="messages"></ContactPage>
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
    },
})

