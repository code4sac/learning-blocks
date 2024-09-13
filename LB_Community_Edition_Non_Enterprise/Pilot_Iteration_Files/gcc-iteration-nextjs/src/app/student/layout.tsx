import SiteNavigationBar from '@/components/layout/navigation/SiteNavigationBar'

let data = {}

let context = {
  auth: undefined!,
  navigationKey: 'example 01',
  queryKey: '1efa02',
}

export default function Layout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <div>
      <SiteNavigationBar siteSelector={true} />
      <div>{children}</div>
    </div>
  )
}
