'use client'
import styles from './DashboardD81.module.css'
import { useState } from 'react'
import { Analytic } from '@/app/_utilities/models/analytics'
import { Demographic } from '@/app/_utilities/models/demographic'
import { TableStudent } from '@/app/_utilities/models/table'
import CardGroupBentoBox from '@/app/_components/ui/card/CardGroupBentoBox'
import CardGroupAnalytics from '@/app/_components/ui/card/CardGroupAnalytics'
import Table01 from '@/app/_components/ui/table/Table01'

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
      <CardGroupBentoBox data={data?.demographics}></CardGroupBentoBox>
      <CardGroupAnalytics
        data={data?.analytics!}
        selectedCategories={selectedCategories}
        selectCategory={selectCategory}
        getCardTheme={getCardTheme}
      ></CardGroupAnalytics>
      <Table01 data={defaultData}></Table01>
    </div>
  )
}

export default DashboardD81
