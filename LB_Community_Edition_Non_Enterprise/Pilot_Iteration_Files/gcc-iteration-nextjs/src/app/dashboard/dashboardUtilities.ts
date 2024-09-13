import { SubMenu } from '@/utility/models/page'

export function parseDashboardNavigationKey(arg0: string | null) {
  switch (arg0) {
    case 'example 01':
      return SubMenu.Example01
      break
    case 'example 02':
      return SubMenu.Example02
      break
    default:
      return SubMenu.Example01
  }
}

export function parseDashboardQueryKey(arg0: string | null) {
  switch (arg0) {
    case 'example 01':
      return SubMenu.Example01
      break
    case 'example 02':
      return SubMenu.Example02
      break
    default:
      return SubMenu.Example01
  }
}
