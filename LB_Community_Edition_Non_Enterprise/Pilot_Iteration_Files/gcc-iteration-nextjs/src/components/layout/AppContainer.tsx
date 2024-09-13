import AppNavigationBar from '@/components/layout/navigation/AppNavigationBar'

interface AppContainerProps {
  selectedMenu: string
  selectedSubMenu: string
  setCurrentSubMenu: any
  children: any
}

/**
 * This container is the content between the navigation bar and the footer. It contains it's own sub navigation bar.
 */
export default function AppContainer({
  children,
  selectedMenu,
  selectedSubMenu,
}: AppContainerProps) {
  return (
    <div>
      <AppNavigationBar
        selectedMenu={selectedMenu}
        selectedSubMenu={selectedSubMenu}
      />
      <div>{children}</div>
    </div>
  )
}
