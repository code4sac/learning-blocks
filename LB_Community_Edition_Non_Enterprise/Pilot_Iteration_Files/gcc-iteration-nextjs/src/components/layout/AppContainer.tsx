import AppNavigationBar from '@/components/layout/navigation/AppNavigationBar'

interface NEAppContainerProps {
  selectedMenu: string
  selectedSubMenu: string
  setCurrentSubMenu: any
  children: any
}

/**
 * Enterprise app container.
 * @param children {ReactElement} Content for the inner application.
 * @param selectedMenu {string} The .
 * @param selectedSubMenu {string} The .
 * @param setCurrentSubMenu {any} The .
 * @returns App container child element.
 */
function AppContainer({
  children,
  selectedMenu,
  selectedSubMenu,
  setCurrentSubMenu,
}: NEAppContainerProps) {
  return (
    <div>
      <AppNavigationBar
        selectedMenu={selectedMenu}
        selectedSubMenu={selectedSubMenu}
        onClickSubMenuLink={setCurrentSubMenu}
      ></AppNavigationBar>
      <div>{children}</div>
    </div>
  )
}

export default AppContainer
