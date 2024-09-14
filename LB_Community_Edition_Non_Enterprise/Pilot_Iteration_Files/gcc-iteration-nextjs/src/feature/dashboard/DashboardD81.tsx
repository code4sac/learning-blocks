'use client'
import { useState } from 'react'

import { Analytic } from '@/utility/models/analytics'
import { Demographic } from '@/utility/models/demographic'
import { TableStudent } from '@/utility/models/table'
import CardGroupBentoBox from '@/components/ui/card/CardGroupBentoBox'
import CardGroupAnalytics from '@/components/ui/card/CardGroupAnalytics'
import Table01 from '@/components/ui/table/Table01'

import styles from './DashboardD81.module.css'

interface PageData {
  analytics?: Analytic[]
  demographics?: Demographic[]
}

export interface D81Props {
  data?: PageData
  setPageQueryKey?: any
}

const defaultData: TableStudent[] = [
  {
    photo: 'a',
    studentId: '99400001',
    name: 'ABBOT, Allan',
    grade: 11,
    gender: 'Male',
    ethnicityCode: 'N',
  },
  {
    photo: 'a',
    studentId: '99400002',
    name: 'ABDELNOUR, Alice',
    grade: 12,
    gender: 'Female',
    ethnicityCode: 'F',
  },
]

/**
 * Heather request dashboard 1. Type "D81".
 * @param subMenu {string} The selected toolbar menu.
 * @returns Dashboard component.
 */
function DashboardD81({ data, setPageQueryKey }: D81Props) {
  const [selectedCategories, setSelectedCategories] = useState(Array<string>)

  function selectCategory(key: string, index: number) {
    setSelectedCategories((it) => [...it, key])
    setPageQueryKey(`${key}${(index + 1) * 20}`)
  }

  function getCardTheme(key: string) {
    if (selectedCategories.includes(key)) {
      return 'dark'
    } else {
      return 'light'
    }
  }

  return (
    <div className={styles.container}>
      <CardGroupBentoBox data={data?.demographics} />
      <CardGroupAnalytics
        data={data?.analytics!}
        getCardTheme={getCardTheme}
        selectCategory={selectCategory}
        selectedCategories={selectedCategories}
      />
      <Table01 data={defaultData} />
    </div>
  )
}

export default DashboardD81
