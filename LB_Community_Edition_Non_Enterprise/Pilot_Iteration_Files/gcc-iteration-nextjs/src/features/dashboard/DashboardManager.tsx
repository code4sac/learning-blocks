import { SubMenu } from '@/utilities/models/page'
import { ReactElement } from 'react'
import DashboardD81 from '@/features/dashboard/DashboardD81'
import DashboardD0f from '@/features/dashboard/DashboardD0F'

export interface DashboardProps {
  data: [any]
  selectedSubMenu: SubMenu
  setPageQueryKey?: any
}

/**
 * Manage routing and data for the dashboard.
 * @param subMenu {string} The selected toolbar menu.
 * @returns App container child element.
 */
function DashboardManager({
  data,
  selectedSubMenu,
  setPageQueryKey,
}: DashboardProps) {
  function renderInnerContent(): ReactElement {
    switch (selectedSubMenu) {
      case SubMenu.Example01:
        return (
          <DashboardD81
            data={data}
            setPageQueryKey={setPageQueryKey}
          ></DashboardD81>
        )
      case SubMenu.Example02:
        return <DashboardD0f demographics={data}></DashboardD0f>
      default:
        return (
          <div>
            <div>
              <div>{selectedSubMenu}</div>
            </div>
          </div>
        )
    }
  }

  return <div>{renderInnerContent()}</div>
}

export default DashboardManager
