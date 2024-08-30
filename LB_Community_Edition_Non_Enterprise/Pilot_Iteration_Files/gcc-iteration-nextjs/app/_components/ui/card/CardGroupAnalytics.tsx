import styles from "./CardGroupAnalytics.module.css";
import CardC79 from "./CardC79";
import CardC93 from "./CardC93";
import { AnalyticCardGroupProps } from "@/app/_utilities/models/card";

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
          case "A9e41":
            return (
              <CardC93
                key={analytic.key}
                data={analytic}
                selectedCategories={selectedCategories}
                getCardTheme={getCardTheme}
                selectCategory={selectCategory}
              ></CardC93>
            );
          default:
            return (
              <CardC79
                key={analytic.key}
                data={analytic}
                selectedCategories={selectedCategories}
                getCardTheme={getCardTheme}
                selectCategory={selectCategory}
              ></CardC79>
            );
        }
      })}
    </div>
  );
}

export default CardGroupAnalytics;
