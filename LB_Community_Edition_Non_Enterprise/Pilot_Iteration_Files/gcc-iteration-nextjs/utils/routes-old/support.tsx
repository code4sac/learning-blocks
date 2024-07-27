import {createFileRoute} from '@tanstack/react-router'
import SupportPage from '../components/pages/SupportPage'

export const Route = createFileRoute('/support')({
    component: () => <div>
        <SupportPage></SupportPage>
    </div>,
    loader: ({context}) => {
        console.log(`Index: ${JSON.stringify(context)}`)
    }
})
