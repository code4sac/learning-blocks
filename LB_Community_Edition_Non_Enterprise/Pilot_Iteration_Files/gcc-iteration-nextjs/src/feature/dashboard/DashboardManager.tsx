import React from 'react'

export interface DashboardManagerProps {
  children: React.ReactNode
  data: [any]
  selectedSubMenu: string
  setPageQueryKey?: any
}

/**
 * DashboardManager component to manage and render different dashboard views
 * based on the selected submenu.
 *
  data,
  selectedSubMenu,
  setPageQueryKey,
 */
export default function DashboardManager({ children }: DashboardManagerProps) {
  return <div>{children}</div>
}
