# Application pages

Pages are the first component to load when a route changes. It is *usually the first and only* component returned from a
FileRoute. To add a new page, create a file with the name [Name]Page.tsx in `src/pages/` folder.

```tsx
import {createFileRoute, redirect} from '@tanstack/react-router'
import DashboardPage from '../components/pages/DashboardPage'
import HomePage from "../components/pages/HomePage.tsx";

export const Route = createFileRoute('/')({
    component: (context) => <div>
        <HomePage navigationKey={context.navigationKey} queryKey={context.queryKey}/>
    </div>
})
```

## Data fetching

This component is a good place to put data fetching. Making API requests at this level allows you to prepare data needed
by the components in the page in one request.
