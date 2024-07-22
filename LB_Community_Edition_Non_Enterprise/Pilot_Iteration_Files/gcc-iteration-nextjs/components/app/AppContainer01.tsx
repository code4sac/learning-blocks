import {SubMenu} from "@/utils/models/page";
import AppNavigationBar01 from "@/components/app/AppNavigationBar01";
import AppInnerContent from "@/components/app/AppInnerContent";
import {ReactElement} from "react";

interface NEAppContainerProps {
  selectedMenu: string
  selectedSubMenu: SubMenu
  setCurrentSubMenu: any
  children: ReactElement
}

/**
 * Enterprise app container.
 * @param children {ReactElement} Content for the inner application.
 * @param selectedMenu {string} The .
 * @param selectedSubMenu {string} The .
 * @param setCurrentSubMenu {any} The .
 * @returns App container child element.
 */
function AppContainer01({children, selectedMenu, selectedSubMenu, setCurrentSubMenu}: NEAppContainerProps) {
  return <div>
    <AppNavigationBar01 selectedMenu={selectedMenu} selectedSubMenu={selectedSubMenu}
                        onClickSubMenuLink={setCurrentSubMenu}></AppNavigationBar01>
    <div>
      <AppInnerContent>
        {children}
      </AppInnerContent>
    </div>
  </div>
}

export default AppContainer01
