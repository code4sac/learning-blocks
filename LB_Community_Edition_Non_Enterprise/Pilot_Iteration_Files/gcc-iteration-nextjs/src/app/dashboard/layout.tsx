import SiteNavigationBar from '@/components/layout/navigation/SiteNavigationBar'

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
