import { createFileRoute, redirect } from '@tanstack/react-router'
import LoginPage from '../components/pages/LoginPage'
import { getRedirectUrl } from '../lib/utils/urlFunctions'

export const Route = createFileRoute('/login')({
    component: () => <div>
        <LoginPage></LoginPage>
    </div>,
    beforeLoad: async ({context, location}) => {
        if (context.auth.isAuthenticated) {
            throw redirect({
                to: `${getRedirectUrl(location)}`
            })
        }
    },
    loader: ({context}) => {
        console.log(`Index: ${context.auth.user}`)
    },
})