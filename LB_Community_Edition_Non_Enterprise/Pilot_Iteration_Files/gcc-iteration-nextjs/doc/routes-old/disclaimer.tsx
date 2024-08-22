import { createFileRoute } from '@tanstack/react-router'
import DisclaimerPage from '../components/pages/DisclaimerPage'

export const Route = createFileRoute('/disclaimer')({
    component: () => <div>
        <DisclaimerPage></DisclaimerPage>
    </div>
})