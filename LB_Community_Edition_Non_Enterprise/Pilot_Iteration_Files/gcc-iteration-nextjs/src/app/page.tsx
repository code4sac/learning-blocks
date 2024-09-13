import SiteNavigationBar from '@/components/layout/navigation/SiteNavigationBar'
import LandingPage02 from '@/feature/landingPage/LandingPage02'

export default async function Page() {
  return (
    <div className="h-screen v-screen">
      <SiteNavigationBar siteSelector={false} />
      <div className="bg-blue-100">
        <LandingPage02 />
      </div>
    </div>
  )
}
