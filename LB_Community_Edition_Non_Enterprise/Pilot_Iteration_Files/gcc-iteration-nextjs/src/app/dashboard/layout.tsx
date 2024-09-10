import SiteNavigationBar from '@/components/layout/navigation/SiteNavigationBar'

export default function Layout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <div>
      <SiteNavigationBar siteSelector={true}></SiteNavigationBar>
      <div>{children}</div>
    </div>
  )
}
