import SiteNavigationBar from '@/app/_components/layout/navigationBar/SiteNavigationBar'

export default function Layout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <div>
      <SiteNavigationBar></SiteNavigationBar>
      <div>{children}</div>
    </div>
  )
}
