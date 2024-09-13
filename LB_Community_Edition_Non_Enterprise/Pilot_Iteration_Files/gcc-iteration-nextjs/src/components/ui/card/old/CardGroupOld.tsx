import { xor } from 'lodash'
import Image from 'next/image'

import styles from './Cards01.module.css'

function CardGroupOld({ data, selectedCards, setSelectedCards, getCardTheme }) {
  return (
    <div className={styles.container}>
      {data?.map((card, index) => {
        return (
          <div key={card.key}>
            <Card
              className={styles.card}
              data-bs-theme={getCardTheme(index)}
              onClick={() => setSelectedCards(xor(selectedCards, [index]))}
            >
              <div onClick={(e) => e.stopPropagation()}>
                <DropdownButton
                  id="dropdown-basic-button"
                  style={{
                    position: 'relative',
                    float: 'right',
                    margin: '4px 8px',
                  }}
                  title={
                    <Image
                      alt="Dropdown menu"
                      height="20"
                      src="menu_dots.png"
                      width="20"
                    />
                  }
                  variant="outline-light"
                >
                  <Dropdown.Item href="#/action-1">
                    View all students
                  </Dropdown.Item>
                  <DropdownDivider />
                  <Dropdown.Item
                    href="#/action-1"
                    onClick={() =>
                      setSelectedCards(xor(selectedCards, [index]))
                    }
                  >
                    Select/unselect
                  </Dropdown.Item>
                  <Dropdown.Item
                    href="#/action-3"
                    onClick={() => setSelectedCards([index])}
                  >
                    Select only {card.title}
                  </Dropdown.Item>
                </DropdownButton>
              </div>
              <Card.Body>
                <Card.Text className={`h6 text-center`}>{card.title}</Card.Text>
                <Image
                  alt={`Chart displaying ${card.levelAmount} level for ${card.title}.`}
                  src={`/${card.analyticsImage}`}
                  width="120"
                />
                {/*<div className={styles.cardBodyImageContainer}>*/}
                {/*    {it.analytics_title === "College and Career" ?*/}
                {/*        : it.analytics_title === "Unduplicated Count" ?*/}
                {/*            <div style={{fontSize: '64px'}}>{it.analytics_level_amount}</div>*/}
                {/*            : <Image src={`/${getAnalyticsChart("", it.analytics_level_amount)}`} width="100"*/}
                {/*                   alt={`Chart displaying ${it.analytics_level_text} level for ${it.analytics_title}.`}/>*/}
                {/*    }*/}
                {/*</div>*/}
                {/*<Card.Text className="text-center">*/}
                {/*    {it.analytics_title === "Unduplicated Count" ?*/}
                {/*        null :*/}
                {/*        it.analytics_level_text}*/}
                {/*</Card.Text>*/}
              </Card.Body>
            </Card>
          </div>
        )
      })}
    </div>
  )
}

export default CardGroupOld
