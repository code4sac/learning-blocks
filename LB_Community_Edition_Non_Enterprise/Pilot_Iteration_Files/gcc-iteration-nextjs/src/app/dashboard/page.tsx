'use client'
import { ReactElement, useState } from 'react'
import { PageProps, SubMenu } from '@/utility/models/page'
import DashboardManager from '@/feature/dashboard/DashboardManager'
import { fetchJson } from '@/service/fetch/fetchJson'
import AppContainer from '@/components/layout/AppContainer'

let data = {}

let context = {
  auth: undefined!,
  navigationKey: 'example 01',
  queryKey: '1efa02',
}

/**
 * Dashboard page.
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
      ></DashboardManager>
    </AppContainer>
  )
}
