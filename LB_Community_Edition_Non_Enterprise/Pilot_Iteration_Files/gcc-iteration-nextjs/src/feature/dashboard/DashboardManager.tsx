import { SubMenu } from '@/utility/models/page'
import { ReactElement } from 'react'
import DashboardD81 from '@/features/dashboard/DashboardD81'
import DashboardD0f from '@/features/dashboard/DashboardD0F'

export interface DashboardManagerProps {
  data: [any]
  selectedSubMenu: SubMenu
  setPageQueryKey?: any
}

/**
 * DashboardManager component to manage and render different dashboard views
 * based on the selected submenu.
 *
 * @param {DashboardManagerProps} props - The props for the DashboardManager component.
 * @returns {ReactElement} The rendered dashboard component.
 */
export default function DashboardManager({
  data,
  selectedSubMenu,
  setPageQueryKey,
}: DashboardManagerProps) {
  return (
    <div>
      <DashboardD81
        data={data}
        setPageQueryKey={setPageQueryKey}
      ></DashboardD81>
      {/* <DashboardD0f demographics={data}></DashboardD0f> */}
    </div>
  )
}
