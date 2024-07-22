import {Demographic} from "@/utils/models/demographic";
import analyticGraphVeryLow from '../../../public/chart_analytics_very_low.png'
import analyticGraphLow from '../../../public/chart_analytics_low.png'
import analyticGraphMedium from '../../../public/chart_analytics_medium.png'
import analyticGraphHigh from '../../../public/chart_analytics_high.png'
import analyticGraphVeryHigh from '../../../public/chart_analytics_very_high.png'
import analyticArrowVeryLow from '../../../public/analytics_red.png'
import analyticArrowLow from '../../../public/analytics_orange.png'
import analyticArrowMedium from '../../../public/analytics_yellow.png'
import analyticArrowHigh from '../../../public/analytics_green.png'
import analyticArrowVeryHigh from '../../../public/analytics_blue.png'

/**
 * Filter the demographics by race code. This excludes demographics like gender and total students.
 * @param demographics
 */
export function parseDemographicPieChartData(demographics: Demographic[]) {
  const a = demographics.filter(it => {
    const firstKeyChar = it.key.charAt(0)
    return firstKeyChar === 'R'
  }).map((it, index) => {
    return {id: index, value: it.demographicAggregate, label: it.demographicTitle}
  })
  return a
}

export function parseAnalyticBarGraphImage(level: number) {
  if (level <= 20) return analyticGraphVeryLow
  else if (level > 20 && level <= 40) return analyticGraphLow
  else if (level > 40 && level <= 60) return analyticGraphMedium
  else if (level > 60 && level <= 80) return analyticGraphHigh
  else return analyticGraphVeryHigh
}

export function parseAnalyticArrowGraphImage(level: number) {
  if (level <= 20) return analyticArrowVeryLow
  else if (level > 20 && level <= 40) return analyticArrowLow
  else if (level > 40 && level <= 60) return analyticArrowMedium
  else if (level > 60 && level <= 80) return analyticArrowHigh
  else return analyticArrowVeryHigh
}

export function a() {
  a
}