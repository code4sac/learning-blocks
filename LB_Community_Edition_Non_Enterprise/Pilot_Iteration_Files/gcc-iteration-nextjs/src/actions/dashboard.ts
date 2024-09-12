'use server'

import { SubMenu } from '@/utility/models/page'
import { fetchJson } from '@/utilities/api/fetchJson'

/**
 * Fetch dashboard data.
 * @see fetchData [Page component documentation](components/pages/README.md#fetchData). Needs update.
 * @returns JSON
 */
export async function getDashboardData(
  pageQueryKey,
  currentSubMenu,
): Promise<JSON> {
  switch (currentSubMenu) {
    case SubMenu.Example01:
      return await fetchJson(
        `${window.location.origin}/api/v1/dashboard/D81/994?filter=${pageQueryKey}`,
      )
    case SubMenu.Example02:
      return await fetchJson(
        `${window.location.origin}/api/v1/dashboard/DemographicsDashboardPage/994`,
      )
    default:
      return await fetchJson(
        `${window.location.origin}/api/v1/dashboard/D81/994`,
      )
  }
}
