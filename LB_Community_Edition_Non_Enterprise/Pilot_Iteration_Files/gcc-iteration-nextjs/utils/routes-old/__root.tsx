import { createRootRouteWithContext, Outlet } from '@tanstack/react-router'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { TanStackRouterDevtools } from '@tanstack/router-devtools'
import { ReactQueryDevtools } from '@tanstack/react-query-devtools'
import 'bootstrap/dist/css/bootstrap.min.css'
import '../index.css'
import SiteNavigationBar from '../components/app/SiteNavigationBar'
import Footer from '../components/app/SiteFooter'
import { AuthenticatedState } from '../auth'
import { fetchAuth } from '../lib/utils/api/user'
import NotFoundPage from '../components/pages/NotFoundPage'

const queryClient = new QueryClient()
let isAuthenticated = false

interface AuthenticatedRouteContext {
    auth: AuthenticatedState
    navigationKey: string
    queryKey: string
}

export const Route = createRootRouteWithContext<AuthenticatedRouteContext>()({
    component: () => <div>
        <QueryClientProvider client={queryClient}>
            <SiteNavigationBar loggedIn={isAuthenticated} />
            <Outlet />
            <Footer />
            <TanStackRouterDevtools />
            <ReactQueryDevtools initialIsOpen={false} />
        </QueryClientProvider>
    </div>,
    beforeLoad: async () => {
        const data = await queryClient.ensureQueryData({
            queryKey: ['auth'],
            queryFn: fetchAuth,
        })
        isAuthenticated = data.isAuthenticated
        return {
            auth: {
                isAuthenticated,
                user: data.user
            }
        }
    },
    notFoundComponent: () => {
        return <div>
            <NotFoundPage />
        </div>
    },
})
