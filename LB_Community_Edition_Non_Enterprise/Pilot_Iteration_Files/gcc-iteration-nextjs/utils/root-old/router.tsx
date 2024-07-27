import {createRouter} from '@tanstack/react-router'
import {routeTree} from './routeTree.gen'

// Uses TanStack Router. https://tanstack.com/router/v1/docs/framework/react/guide/file-based-routing
// Use the context object to add context to routes. They will be typesafe.
const router = createRouter({
    routeTree,
    context: {
        auth: undefined!,
        navigationKey: 'example 01',
        queryKey: '1efa02',
    }
})

export default router