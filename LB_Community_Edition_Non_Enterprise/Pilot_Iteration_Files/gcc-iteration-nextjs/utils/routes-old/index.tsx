import {createFileRoute, redirect} from '@tanstack/react-router'
import HomePage from "../components/pages/HomePage.tsx";

export const Route = createFileRoute('/')({
    component: (context) => <div>
        <HomePage navigationKey={context.navigationKey} queryKey={context.queryKey}/>
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
            //context.navigationKey =    location.searchStr.match('QueryKey')
        }
        return context
    },
    loader: ({context}) => {
        console.log(`%cA colorful example of logging context: ${JSON.stringify(context)}`, "color:" + (context.auth.isAuthenticated ? 'green' : 'red') + ";");
    },
})

