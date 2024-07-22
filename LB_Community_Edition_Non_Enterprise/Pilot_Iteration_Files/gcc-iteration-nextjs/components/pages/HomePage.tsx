import DashboardPage from './DashboardPage'
import {PageProps} from "@/utils/models/page";

/**
 * Home page.
 * @returns JSX element.
 */
function HomePage({navigationKey, queryKey}: PageProps) {
  let element = <div>
    <DashboardPage/>
  </div>

  return element
}

export default HomePage