import { createFileRoute, redirect } from '@tanstack/react-router'
import DashboardPage from '../components/pages/DashboardPage'

export const Route = createFileRoute('/dashboard')({
    component: (context) => <div>
        <DashboardPage navigationKey={context.navigationKey} queryKey={context.queryKey}></DashboardPage>
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
        if (location.searchStr) {
            //context.navigationKey = location.searchStr.match('NavigationKey')
            //context.navigationKey = location.searchStr.match('QueryKey')
        }
        return context
    },
})

