import { useState } from 'react'
import AppContainer02 from '../components/app/AppContainer02.js'

export interface MessagesPageProps {
  selectedSubMenu: string
}

/**
 * Contact page.
 */
export default function MessagesPage({ selectedSubMenu }: MessagesPageProps) {
  const [currentSubMenu, setCurrentSubMenu] = useState('contact')

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
        selectedMenu="messages"
        selectedSubMenu={currentSubMenu}
        setCurrentSubMenu={setCurrentSubMenu}
      >
        {renderDashboardInnerContent(currentSubMenu)}
      </AppContainer02>
    </div>
  )
}

export default MessagesPage
