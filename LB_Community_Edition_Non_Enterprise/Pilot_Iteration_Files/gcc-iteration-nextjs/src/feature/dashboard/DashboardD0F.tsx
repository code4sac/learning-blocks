'use client'
import { Demographic } from '@/utility/models/demographic'
import CardC44 from '@/components/ui/card/CardC44'
import CardC89 from '@/components/ui/card/CardC89'

import styles from './DashboardD0F.module.css'

export interface D0fProps {
  demographics: [Demographic]
}

/**
 * Demographic dashboard. Type "D0f".
 * @param subMenu {string} The selected toolbar menu.
 * @returns App container child element.
 */
function DashboardD0f({ demographics }: D0fProps) {
  return (
    <div>
      <div className={styles.demographicAggregateContainer}>
        <div className={`${styles.demographicCard} ${styles.demographic1}`}>
          {demographics
            .filter((it) => it.key == 'T1')
            .map((it) => (
              <CardC44
                key={it.key}
                stat={it.demographicAggregate.toString()}
                title={it.demographicTitle}
              />
            ))}
        </div>
        <div className={`${styles.demographicCard} ${styles.demographic2}`}>
          {demographics
            .filter((it) => it.key == 'G1')
            .map((it) => (
              <CardC44
                key={it.key}
                stat={it.demographicAggregate.toString()}
                title={it.demographicTitle}
              />
            ))}
        </div>
        <div className={`${styles.demographicCard} ${styles.demographic3}`}>
          {demographics
            .filter((it) => it.key == 'G2')
            .map((it) => (
              <CardC44
                key={it.key}
                stat={it.demographicAggregate.toString()}
                title={it.demographicTitle}
              />
            ))}
        </div>
        <div className={`${styles.demographicCard} ${styles.demographic4}`}>
          {demographics
            .filter((it) => it.key == 'G3')
            .map((it) => (
              <CardC44
                key={it.key}
                stat={it.demographicAggregate.toString()}
                title={it.demographicTitle}
              />
            ))}
        </div>
        <div className={`${styles.demographicCard} ${styles.demographic5}`}>
          <CardC89 data={demographics} />
        </div>
        <div className={`${styles.demographicCard} ${styles.demographic6}`} />
        <div className={`${styles.demographicCard} ${styles.demographic7}`} />
        <div className={`${styles.demographicCard} ${styles.demographic8}`} />
        <div className={`${styles.demographicCard} ${styles.demographic9}`} />
        <div className={`${styles.demographicCard} ${styles.demographic10}`} />
      </div>
    </div>
  )
}

export default DashboardD0f
