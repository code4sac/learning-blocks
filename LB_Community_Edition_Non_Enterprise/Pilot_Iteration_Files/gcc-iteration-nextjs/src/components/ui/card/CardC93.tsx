import Image from 'next/image'

import { parseAnalyticBarGraphImage } from '@/feature/dashboard/graphUtils'
import { AnalyticCategory } from '@/utility/models/analytics'
import { AnalyticCardProps } from '@/utility/models/card'

import styles from './CardC93.module.css'

/**
 * Dashboard bar graph card. Categories (Very Low, Low, Medium, High, Very High). Monotone color theme.
 * @param param0
 * @returns
 */
function CardC93({
  data,
  selectedCategories,
  getCardTheme,
  selectCategory,
}: AnalyticCardProps) {
  function getCategoryName(index: number) {
    switch (index) {
      case 0:
        return 'Very Low'
      case 1:
        return 'Low'
      case 2:
        return 'Medium'
      case 3:
        return 'High'
      case 4:
        return 'Very High'
    }
  }

  return (
    <div>
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
              src={parseAnalyticBarGraphImage(data.analyticLevelAmount)}
              width="120"
            />
          </div>
          <div className={styles.categoriesContainer}>
            {data.analyticCategories?.map(
              (category: AnalyticCategory, index: number) => {
                return (
                  <div
                    key={category.key}
                    className={styles.categoryCard}
                    data-bs-theme={getCardTheme(index)}
                    onClick={() => selectCategory(data.key, index)}
                  >
                    <div>
                      <div className={styles.categoryAmountText}>
                        {category.analyticCategoryStudentAmount}
                      </div>
                      <div className={styles.categoryNameText}>
                        {getCategoryName(index)}
                      </div>
                    </div>
                  </div>
                )
              },
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

export default CardC93
