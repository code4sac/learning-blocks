import { Analytic } from './analytics.js'
import { Demographic } from './demographic.js'

export interface CardProps {
  data?: any
  selectedCategories?: any
  getCardTheme?: any
  selectCategory?: any
}

/**
 * Analytic card groups use a list of Analytics as data.
 */
export interface AnalyticCardGroupProps extends CardProps {
  data?: Analytic[]
}

/**
 * Analytic card uses an Analytic as data.
 */
export interface AnalyticCardProps extends CardProps {
  data?: Analytic
}

/**
 * Demographic card groups use a list of Demographics as data.
 */
export interface DemographicCardGroupProps extends CardProps {
  data?: Demographic[]
}

/**
 * Demographic card uses a Demographic as data.
 */
export interface DemographicCardProps extends CardProps {
  data?: Demographic
}
