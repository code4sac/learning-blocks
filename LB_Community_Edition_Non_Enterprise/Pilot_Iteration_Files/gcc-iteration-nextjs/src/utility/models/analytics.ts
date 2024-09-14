export interface Analytic {
  key: string
  analyticTitle: string
  analyticLevelAmount: number
  analyticLevelText: string
  analyticDescription: string
  analyticCategories: AnalyticCategory[]
}

export interface AnalyticCategory {
  key: string
  analyticCategoryStudentAmount: number
}
