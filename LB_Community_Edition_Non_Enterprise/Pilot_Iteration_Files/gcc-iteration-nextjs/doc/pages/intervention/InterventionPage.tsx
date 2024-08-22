import { useState } from 'react'
import AppContainer02 from '../components/app/AppContainer02.jsx'

/**
 * Messages page.
 */
function InterventionPage() {
    const [currentSubMenu, setCurrentSubMenu] = useState('IEP')

    function renderDashboardInnerContent(selectedSubMenu) {
        switch (selectedSubMenu) {
            case 'example 01':
                return <div>{currentSubMenu}</div>
            default:
                return <div>{currentSubMenu}</div>
        }
    }

    return <div>
        <AppContainer02 selectedMenu="intervention" selectedSubMenu={currentSubMenu}
                        setCurrentSubMenu={setCurrentSubMenu}>
            {renderDashboardInnerContent(currentSubMenu)}
        </AppContainer02>
    </div>
}

export default InterventionPage