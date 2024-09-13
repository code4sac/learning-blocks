import Image from 'next/image'

import { AnalyticCardProps } from '@/utility/models/card'
import { parseAnalyticArrowGraphImage } from '@/feature/dashboard/graphUtils'

import styles from './CardC79.module.css'

/**
 * Dashboard arrow graph card. Categories (Red, Orange, Yellow, Green, Blue). Monotone color theme.
 * @param props Card component properties.
 * @returns Single arrow graph data.
 */
function CardC79({
  data,
  selectedCategories,
  getCardTheme,
  selectCategory,
}: AnalyticCardProps) {
  function getColorIndicator(index: number) {
    switch (index) {
      case 0:
        return styles.colorIndicator0
      case 1:
        return styles.colorIndicator1
      case 2:
        return styles.colorIndicator2
      case 3:
        return styles.colorIndicator3
      case 4:
        return styles.colorIndicator4
    }
  }

  return (
    <div key={data.key}>
      <div>
        <div>
          <div className={`h6 text-center ${styles.cardBodyImageContainer}`}>
            {data.analyticTitle}
            <div
              delay={{ show: 250, hide: 400 }}
              overlay={(props) => (
                <div id="button-tooltip" {...props}>
                  {data.analyticDescription}
                </div>
              )}
              placement="right"
            >
              <Image
                alt={`Hover for more info about ${data.analyticTitle}`}
                className={styles.helpIcon}
                height={24}
                src="menu_help.svg"
                width={24}
              />
            </div>
          </div>
          <div className={styles.cardBodyImageContainer}>
            <Image
              alt={`Chart displaying ${data.analyticLevelAmount} level for ${data.analyticDescription}.`}
              src={parseAnalyticArrowGraphImage(data.analyticLevelAmount)}
              width="120"
            />
          </div>
          <div className={styles.categoriesContainer}>
            {data.analyticCategories?.map((category, index) => {
              return (
                <div
                  key={category.key}
                  className={styles.categoryCard}
                  data-bs-theme={getCardTheme(index)}
                  onClick={() => selectCategory(data.key, index)}
                >
                  <div className={getColorIndicator(index)} />
                  <div>{category.analyticCategoryStudentAmount}</div>
                </div>
              )
            })}
          </div>
        </div>
      </div>
    </div>
  )
}

export default CardC79
