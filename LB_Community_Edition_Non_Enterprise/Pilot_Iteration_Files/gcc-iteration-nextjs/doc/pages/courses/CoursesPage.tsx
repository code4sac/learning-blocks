import { useState } from 'react'
import AppContainer02 from '../components/app/AppContainer02.jsx'

/**
 * Courses page.
 */
function CoursesPage() {
    const [currentSubMenu, setCurrentSubMenu] = useState('schedule')

    function renderDashboardInnerContent(selectedSubMenu) {
        switch (selectedSubMenu) {
            case 'example 01':
                return <div>{currentSubMenu}</div>
            default:
                return <div>{currentSubMenu}</div>
        }
    }

    return <div>
        <AppContainer02 selectedMenu="courses" selectedSubMenu={currentSubMenu} setCurrentSubMenu={setCurrentSubMenu}>
            {renderDashboardInnerContent(currentSubMenu)}
        </AppContainer02>
    </div>
}

export default CoursesPage