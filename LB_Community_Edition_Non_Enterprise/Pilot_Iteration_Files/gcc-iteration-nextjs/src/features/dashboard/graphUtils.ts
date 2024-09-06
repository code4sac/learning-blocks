import { Demographic } from '@/utilities/models/demographic'

/**
 * Filter the demographics by race code. This excludes demographics like gender and total students.
 * @param demographics
 */
export function parseDemographicPieChartData(demographics: Demographic[]) {
  const a = demographics
    .filter((it) => {
      const firstKeyChar = it.key.charAt(0)
      return firstKeyChar === 'R'
    })
    .map((it, index) => {
      return {
        id: index,
        value: it.demographicAggregate,
        label: it.demographicTitle,
      }
    })
  return a
}

export function parseAnalyticBarGraphImage(level: number) {
  if (level <= 20) return 'chart_analytics_very_low.png'
  else if (level > 20 && level <= 40) return 'chart_analytics_low.png'
  else if (level > 40 && level <= 60) return 'chart_analytics_medium.png'
  else if (level > 60 && level <= 80) return 'chart_analytics_high.png'
  else return 'chart_analytics_very_high.png'
}

export function parseAnalyticArrowGraphImage(level: number) {
  if (level <= 20) return 'analytic_arrow_very_low.png'
  else if (level > 20 && level <= 40) return 'analytic_arrow_low.png'
  else if (level > 40 && level <= 60) return 'analytic_arrow_medium.png'
  else if (level > 60 && level <= 80) return 'analytic_arrow_high.png'
  else return 'analytic_arrow_very_high.png'
}

export function a() {
  a
}
