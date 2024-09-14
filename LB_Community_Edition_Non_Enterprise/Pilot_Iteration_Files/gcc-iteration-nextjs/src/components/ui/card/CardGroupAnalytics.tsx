import { AnalyticCardGroupProps } from '@/utility/models/card'

import styles from './CardGroupAnalytics.module.css'
import CardC79 from './CardC79'
import CardC93 from './CardC93'

function CardGroupAnalytics({
  data,
  selectedCategories,
  getCardTheme,
  selectCategory,
}: AnalyticCardGroupProps) {
  return (
    <div className={styles.container}>
      {data?.map((analytic) => {
        switch (analytic.key) {
          case 'A9e41':
            return (
              <CardC93
                key={analytic.key}
                data={analytic}
                getCardTheme={getCardTheme}
                selectCategory={selectCategory}
                selectedCategories={selectedCategories}
              />
            )
          default:
            return (
              <CardC79
                key={analytic.key}
                data={analytic}
                getCardTheme={getCardTheme}
                selectCategory={selectCategory}
                selectedCategories={selectedCategories}
              />
            )
        }
      })}
    </div>
  )
}

export default CardGroupAnalytics
