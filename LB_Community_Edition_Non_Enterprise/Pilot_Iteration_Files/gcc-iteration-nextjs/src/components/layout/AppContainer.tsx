import AppNavigationBar from '@/components/layout/navigation/AppNavigationBar'
import { SubMenu } from '@/utility/models/page'

interface AppContainerProps {
  selectedMenu: string
  selectedSubMenu: SubMenu
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
export default function AppContainer({
  children,
  selectedMenu,
  selectedSubMenu,
  setCurrentSubMenu,
}: AppContainerProps) {
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
