import { useState } from 'react'
import AppContainer01 from '@/components/layout/AppContainer.jsx'
import { Container } from 'react-bootstrap'

/**
 * Student page.
 * @returns App page.
 */
export default function StudentPage() {
  const [currentSubMenu, setCurrentSubMenu] = useState('Personal Info')

  /**
   * Handle app logic and render the inner app content.
   * @param selectedSubMenu {string} The selected toolbar menu.
   * @returns App container child element.
   */
  function renderDashboardInnerContent(selectedSubMenu) {
    switch (selectedSubMenu) {
      case 'example 01':
        return <div>{currentSubMenu}</div>
      default:
        return <Container>{currentSubMenu}</Container>
    }
  }

  // Success 📺
  return (
    <div>
      <AppContainer01
        selectedMenu="student"
        selectedSubMenu={currentSubMenu}
        setCurrentSubMenu={setCurrentSubMenu}
      >
        {renderDashboardInnerContent(currentSubMenu)}
      </AppContainer01>
    </div>
  )
}
