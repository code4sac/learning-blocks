'use client'

import { useSearchParams } from 'next/navigation'

import DashboardManager from '@/feature/dashboard/DashboardManager'
import AppContainer from '@/components/layout/AppContainer'

export default function Page({ params }: { params: { menu: string } }) {
  let searchParams = useSearchParams()
  let currentSubMenu = searchParams.get('q') || '1efa02'
  let data = undefined

  return (
    <AppContainer selectedMenu={params.menu} selectedSubMenu={currentSubMenu}>
      <DashboardManager
        data={data ? data : [{}]}
        selectedSubMenu={currentSubMenu}
      />
    </AppContainer>
  )
}
