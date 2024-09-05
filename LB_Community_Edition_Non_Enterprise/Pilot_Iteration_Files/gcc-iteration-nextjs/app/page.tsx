import SiteNavigationBar from '@/app/_components/layout/navigationBar/SiteNavigationBar'
import LandingPage02 from '@/app/_features/landingPage/LandingPage02'

export default async function Page() {
  return (
    <div className="h-screen v-screen">
      <SiteNavigationBar siteSelector={false}></SiteNavigationBar>
      <div className="bg-blue-100">
        <LandingPage02></LandingPage02>
      </div>
    </div>
  )
}
