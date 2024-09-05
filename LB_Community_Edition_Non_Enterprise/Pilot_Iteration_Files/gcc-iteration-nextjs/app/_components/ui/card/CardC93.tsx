import styles from './CardC93.module.css'
import { parseAnalyticBarGraphImage } from '@/app/_utilities/graph/graphUtils'
import { AnalyticCategory } from '@/app/_utilities/models/analytics'
import { AnalyticCardProps } from '@/app/_utilities/models/card'
import Image from 'next/image'

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
              src={parseAnalyticBarGraphImage(data.analyticLevelAmount)}
              width="120"
              alt={`Chart displaying ${data.analyticLevelAmount} level for ${data.analyticDescription}.`}
            />
          </div>
          <div className={styles.categoriesContainer}>
            {data.analyticCategories?.map(
              (category: AnalyticCategory, index: number) => {
                return (
                  <div
                    className={styles.categoryCard}
                    key={category.key}
                    onClick={() => selectCategory(data.key, index)}
                    data-bs-theme={getCardTheme(index)}
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
