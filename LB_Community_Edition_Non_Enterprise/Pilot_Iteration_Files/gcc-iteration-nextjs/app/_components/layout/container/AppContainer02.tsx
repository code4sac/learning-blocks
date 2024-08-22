import AppNavigationBar02 from "@/app/_components/layout/navigationBar/AppNavigationBar02";

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
function AppContainer02({children, selectedMenu, selectedSubMenu, setCurrentSubMenu}: NEAppContainerProps) {
    return <div>
        <AppNavigationBar02 selectedMenu={selectedMenu} selectedSubMenu={selectedSubMenu}
                            onClickSubMenuLink={setCurrentSubMenu}></AppNavigationBar02>
        <div>
            {children}
        </div>
    </div>
}

export default AppContainer02
