import { useState } from 'react'
import AppContainer02 from '../components/app/AppContainer02.jsx'

/**
 * Pathway page.
 */
export default function PathwayPage() {
  const [currentSubMenu, setCurrentSubMenu] = useState('tests')

  function renderDashboardInnerContent(selectedSubMenu) {
    switch (selectedSubMenu) {
      case 'example 01':
        return <div>{currentSubMenu}</div>
      default:
        return <div>{currentSubMenu}</div>
    }
  }

  return (
    <div>
      <AppContainer02
        selectedMenu="pathway"
        selectedSubMenu={currentSubMenu}
        setCurrentSubMenu={setCurrentSubMenu}
      >
        {renderDashboardInnerContent(currentSubMenu)}
      </AppContainer02>
    </div>
  )
}

export default PathwayPage
