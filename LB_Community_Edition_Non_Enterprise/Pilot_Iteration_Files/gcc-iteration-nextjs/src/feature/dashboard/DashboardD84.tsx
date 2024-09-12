'use client'
import { Card } from 'react-bootstrap'
import data from '../../../__tests__/mock/ExampleDataAnalytics.json'
import styles from './DashboardD84.module.css'
import { xor } from 'lodash'
import { useState } from 'react'
import { Demographic } from '@/utility/models/demographic'
import Image from 'next/image'

export interface D84Props {
  demographics: [Demographic]
}

/**
 * Heather request dashboard 1. Type "D84".
 * @param subMenu {string} The selected toolbar menu.
 * @returns App container child element.
 */
function DashboardD84() {
  const [selectedCards, setSelectedCards] = useState(Array<number>)

  function getAnalyticsChart(type: string, levelAmount: number): string {
    if (type === 'chart') {
      if (levelAmount <= 20) {
        return 'chart_analytics_very_low.png'
      } else if (levelAmount <= 40) {
        return 'chart_analytics_low.png'
      } else if (levelAmount <= 60) {
        return 'chart_analytics_medium.png'
      } else if (levelAmount <= 80) {
        return 'chart_analytics_high.png'
      } else if (levelAmount <= 100) {
        return 'chart_analytics_very_high.png'
      } else {
        return ''
      }
    } else if (type === 'standardsMet') {
      return ''
    } else {
      if (levelAmount <= 20) {
        return 'analytics_red.png'
      } else if (levelAmount <= 40) {
        return 'analytics_orange.png'
      } else if (levelAmount <= 60) {
        return 'analytics_yellow.png'
      } else if (levelAmount <= 80) {
        return 'analytics_green.png'
      } else if (levelAmount <= 100) {
        return 'analytics_blue.png'
      } else {
        return ''
      }
    }
  }

  function handleClick(id: number) {
    setSelectedCards(xor(selectedCards, [id]))
  }

  function getCardTheme(id: number) {
    if (selectedCards.includes(id)) {
      return 'dark'
    } else {
      return 'light'
    }
  }

  return (
    <div className={styles.container}>
      {data.map((it, index) => {
        return (
          <Card
            key={it.key}
            className={styles.card}
            onClick={() => handleClick(index)}
            data-bs-theme={getCardTheme(index)}
          >
            {/*<DropdownButton id="dropdown-basic-button" title={<Image src="/menu_dots.png" height="20" width="20" /> }*/}
            {/*  style={{ position: 'relative', float: 'right', margin: '4px 8px' }}*/}
            {/*  variant='outline-light'*/}
            {/*>*/}
            {/*  <Dropdown.Item href="#/action-1">Action</Dropdown.Item>*/}
            {/*  <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>*/}
            {/*  <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>*/}
            {/*  <DropdownDivider />*/}
            {/*  <Dropdown.Item href="#/action-1">Select/Unselect</Dropdown.Item>*/}
            {/*  <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>*/}
            {/*  <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>*/}
            {/*</DropdownButton>*/}
            <Card.Body>
              <Card.Text className={`h6 text-center`}>
                {it.analytics_title}
              </Card.Text>
              <div className={styles.cardBodyImageContainer}>
                {it.analytics_title === 'College and Career' ? (
                  <Image
                    src={`/${getAnalyticsChart(
                      'chart',
                      it.analytics_level_amount,
                    )}`}
                    width="120"
                    alt={`Chart displaying ${it.analytics_level_text} level for ${it.analytics_title}.`}
                  />
                ) : it.analytics_title === 'Unduplicated Count' ? (
                  <div style={{ fontSize: '64px' }}>
                    {it.analytics_level_amount}
                  </div>
                ) : (
                  <Image
                    src={`/${getAnalyticsChart('', it.analytics_level_amount)}`}
                    width="100"
                    alt={`Chart displaying ${it.analytics_level_text} level for ${it.analytics_title}.`}
                  />
                )}
              </div>
              <Card.Text className="text-center">
                {it.analytics_title === 'Unduplicated Count'
                  ? null
                  : it.analytics_level_text}
              </Card.Text>
            </Card.Body>
          </Card>
        )
      })}
    </div>
  )
}

export default DashboardD84
