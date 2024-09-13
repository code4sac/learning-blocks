'use client'
import { useState } from 'react'

import { PageProps, SubMenu } from '@/utility/models/page'
import DashboardManager from '@/feature/dashboard/DashboardManager'
import AppContainer from '@/components/layout/AppContainer'

/**
 * Student page.
 * @returns App page.
 */
export default function Page({ navigationKey, queryKey }: PageProps) {
  const [currentSubMenu, setCurrentSubMenu] = useState(SubMenu.Example01)
  const [pageQueryKey, setPageQueryKey] = useState(queryKey ? queryKey : '')
  return (
    <AppContainer
      selectedMenu="dashboard"
      selectedSubMenu={currentSubMenu}
      setCurrentSubMenu={setCurrentSubMenu}
    >
      <DashboardManager
        data={data ? data : [{}]}
        selectedSubMenu={currentSubMenu}
      />
    </AppContainer>
  )
}
