import SiteNavbar from '@/components/layout/SiteNavbar'
import SiteFooter from '@/components/layout/SiteFooter'
import LandingPage02 from '@/feature/landingPage/LandingPage02'

export default async function Page() {
  return (
    <div className="h-screen v-screen">
      <div className="flex flex-col min-h-screen">
        <SiteNavbar loggedIn={false} />
        <main>
          <LandingPage02 />
        </main>
        <footer className="mt-auto">
          <SiteFooter />
        </footer>
      </div>
    </div>
  )
}
