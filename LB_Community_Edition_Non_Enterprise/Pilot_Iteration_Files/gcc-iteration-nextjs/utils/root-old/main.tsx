import {StrictMode} from 'react'
import ReactDOM from 'react-dom/client'
import {RouterProvider} from '@tanstack/react-router'
import {AuthProvider, useAuth} from './lib/models/auth'
import router from './router'

declare module '@tanstack/react-router' {
    interface Register {
        router: typeof router
    }
}

/**
 * Uses Tanstack router.
 * - File-based routing: The default layout is `routes/__root.tsx`.
 * @see https://tanstack.com/router/v1/docs/framework/react/guide/file-based-routing
 */
function InnerApp(): JSX.Element {
    const auth = useAuth()
    return <RouterProvider router={router} context={{auth}}/>
}

/**
 * Main application component. Configure providers that are needed by the router.
 * - Authenticated route provider with user context.
 */
function App(): JSX.Element {
    return <AuthProvider>
        <InnerApp/>
    </AuthProvider>
}

/**
 * This is the entry-point for the application.
 * - <StrictMode>: This makes the page refresh twice on first load in development.
 * @param root The root HTML element to attach the React application.
 */
function renderApp(rootElement: HTMLElement): void {
    const root = ReactDOM.createRoot(rootElement)
    root.render(
        <StrictMode>
            <App/>
        </StrictMode>
    )
}

const rootElement = document.getElementById('root')!
if (!rootElement.innerHTML) {
    renderApp(rootElement)
} else {
    console.log('Main.tsx debug: HTML element not found.')
}
