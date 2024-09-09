'use client'
import { ReactElement, useState } from 'react'
import { PageProps, SubMenu } from '@/utilities/models/page'
import DashboardManager from '@/features/dashboard/DashboardManager'
import { fetchJson } from '@/services/fetch/fetchJson'
import AppContainer from '@/components/layout/AppContainer'

let data = {}

let context = {
  auth: undefined!,
  navigationKey: 'example 01',
  queryKey: '1efa02',
}

/**
 * Dashboard page.
 * @returns App page.
 */
function DashboardPage({ navigationKey, queryKey }: PageProps) {
  const [currentSubMenu, setCurrentSubMenu] = useState(SubMenu.Example01)
  const [pageQueryKey, setPageQueryKey] = useState(queryKey ? queryKey : '')

  // const { isPending, isError, error, data, isFetching, isPlaceholderData } = useQuery({
  //   queryKey: [pageQueryKey],
  //   queryFn: () => fetchData(),
  //   placeholderData: keepPreviousData
  // })

  /**
   * Handle app logic and render the inner app content.
   * @see renderInnerContent [Page component documentation](components/pages/README.md#arenderInnerContent)
   * @returns App container child element.
   */
  function renderInnerContent(): ReactElement {
    switch (currentSubMenu) {
      case SubMenu.Example01:
        return (
          <DashboardManager
            data={data}
            selectedSubMenu={currentSubMenu}
            setPageQueryKey={setPageQueryKey}
          ></DashboardManager>
        )
      case SubMenu.Example02:
        return (
          <DashboardManager
            data={data}
            selectedSubMenu={currentSubMenu}
          ></DashboardManager>
        )
      default:
        return (
          <DashboardManager
            data={data}
            selectedSubMenu={SubMenu.Example01}
          ></DashboardManager>
        )
    }
  }

  /**
   * Fetch dashboard data.
   * @see fetchData [Page component documentation](components/pages/README.md#fetchData). Needs update.
   * @returns JSON
   */
  async function fetchData(): Promise<JSON> {
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

  return (
    <div>
      <AppContainer
        selectedMenu="dashboard"
        selectedSubMenu={currentSubMenu}
        setCurrentSubMenu={setCurrentSubMenu}
      >
        <DashboardManager
          data={data ? data : [{}]}
          selectedSubMenu={currentSubMenu}
        ></DashboardManager>
      </AppContainer>
      {/* {isPending ? <AppContainer selectedMenu="dashboard" selectedSubMenu={currentSubMenu}
      setCurrentSubMenu={setCurrentSubMenu}>
      <DashboardManager data={data ? data : [{}]} selectedSubMenu={currentSubMenu}></DashboardManager>
    </AppContainer>
      : isError ? <Container>
        <Row className="justify-content-md-center">
          <Col>An error has occurred: + {error.message}</Col>
        </Row>
      </Container>
        : <div>
          <AppContainer02 selectedMenu="dashboard" selectedSubMenu={currentSubMenu}
            setCurrentSubMenu={setCurrentSubMenu}>
            {isFetching ? <span> Loading...</span> : null}{' '}

            {renderInnerContent()}
          </AppContainer02>
        </div>} */}
    </div>
  )
}
