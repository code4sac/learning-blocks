'use client'

import { useSearchParams } from 'next/navigation'

import AppContainer from '@/components/layout/AppContainer'
import LoadingSkeleton from '@/components/ui/skeleton/LoadingSkeleton'

export default function Loader({ params }: { params: { menu: string } }) {
  let searchParams = useSearchParams()
  let currentSubMenu = searchParams.get('navigationKey') || ''

  return (
    <AppContainer selectedMenu={params.menu} selectedSubMenu={currentSubMenu}>
      return <LoadingSkeleton />
    </AppContainer>
  )
}
