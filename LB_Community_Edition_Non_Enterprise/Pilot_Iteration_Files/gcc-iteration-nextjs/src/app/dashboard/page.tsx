'use client'

import { useSearchParams } from 'next/navigation'

import DashboardManager from '@/feature/dashboard/DashboardManager'
import AppContainer from '@/components/layout/AppContainer'

export default function Page() {
  let searchParams = useSearchParams()
  let currentSubMenu = searchParams.get('navigationKey') || ''
  let data = undefined

  return (
    <AppContainer selectedMenu="dashboard" selectedSubMenu={currentSubMenu}>
      <DashboardManager
        data={data ? data : [{}]}
        selectedSubMenu={currentSubMenu}
      />
    </AppContainer>
  )
}
