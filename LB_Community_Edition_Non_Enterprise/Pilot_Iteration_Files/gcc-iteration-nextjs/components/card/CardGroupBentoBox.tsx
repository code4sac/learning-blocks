import styles from './CardGroupBentoBox.module.css'
import {DemographicCardGroupProps} from "@/utils/models/card";
import CardC89 from "@/components/card/CardC89";

function CardGroupBentoBox({data}: DemographicCardGroupProps) {
  return <div className={styles.container}>
    <CardC89 data={data}></CardC89>
  </div>
}

export default CardGroupBentoBox