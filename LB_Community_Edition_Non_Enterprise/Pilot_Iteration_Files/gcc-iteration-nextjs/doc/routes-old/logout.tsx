import { createFileRoute } from '@tanstack/react-router'
import LogoutPage from '../components/pages/LogoutPage'

export const Route = createFileRoute('/logout')({
    component: () => <div>
        <LogoutPage></LogoutPage>
    </div>,
    loader: ({context}) => {
        console.log(`Index: ${context.auth.user}`)
    }
})