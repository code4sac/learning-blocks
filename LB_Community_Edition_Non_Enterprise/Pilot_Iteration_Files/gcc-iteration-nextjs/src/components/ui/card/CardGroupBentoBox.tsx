import { DemographicCardGroupProps } from '@/utility/models/card'
import CardC89 from '@/components/ui/card/CardC89'

import styles from './CardGroupBentoBox.module.css'

function CardGroupBentoBox({ data }: DemographicCardGroupProps) {
  return (
    <div className={styles.container}>
      <CardC89 data={data} />
    </div>
  )
}

export default CardGroupBentoBox
