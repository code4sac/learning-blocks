import {createFileRoute, redirect} from '@tanstack/react-router'
import SettingsPage from '../components/pages/SettingsPage'

export const Route = createFileRoute('/settings')({
    component: () => <div>
        <SettingsPage></SettingsPage>
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
    }
})