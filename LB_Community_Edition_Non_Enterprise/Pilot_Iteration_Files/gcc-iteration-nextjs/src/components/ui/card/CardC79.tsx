import styles from './CardC79.module.css'
import Image from 'next/image'
import { AnalyticCardProps } from '@/utility/models/card'
import { parseAnalyticArrowGraphImage } from '@/feature/dashboard/graphUtils'

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
              placement="right"
              delay={{ show: 250, hide: 400 }}
              overlay={(props) => (
                <div id="button-tooltip" {...props}>
                  {data.analyticDescription}
                </div>
              )}
            >
              <Image
                src="menu_help.svg"
                className={styles.helpIcon}
                alt={`Hover for more info about ${data.analyticTitle}`}
                height={24}
                width={24}
              />
            </div>
          </div>
          <div className={styles.cardBodyImageContainer}>
            <Image
              src={parseAnalyticArrowGraphImage(data.analyticLevelAmount)}
              width="120"
              alt={`Chart displaying ${data.analyticLevelAmount} level for ${data.analyticDescription}.`}
            />
          </div>
          <div className={styles.categoriesContainer}>
            {data.analyticCategories?.map((category, index) => {
              return (
                <div
                  className={styles.categoryCard}
                  key={category.key}
                  onClick={() => selectCategory(data.key, index)}
                  data-bs-theme={getCardTheme(index)}
                >
                  <div className={getColorIndicator(index)}></div>
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
