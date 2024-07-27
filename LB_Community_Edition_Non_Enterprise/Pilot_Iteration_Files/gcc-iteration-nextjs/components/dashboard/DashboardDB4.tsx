"use client";
import { Container } from 'react-bootstrap'
import styles from './DashboardDb4.module.css'
import { reject, xor } from 'lodash'
import { useState } from 'react'
import CardC44 from "@/components/card/CardC44";
import CardC89 from "@/components/card/CardC89";

export interface DashboardAggregatorProps {
  languageStudents: [LanguageStudent]
}

export interface LanguageStudent {
  languageStudentTitle: string
  key: string
  languageStudentAggregate: number
}

function DashboardDb4({ languageStudents }: DashboardAggregatorProps) {
  const [selectedCards, setSelectedCards] = useState([0])

  function handleClick(id: number) {
    if (id === 0) {
      setSelectedCards([0])
    } else {
      if (selectedCards.length === 1 && selectedCards[0] === id) {
        setSelectedCards([0])
      } else {
        setSelectedCards(xor(reject(selectedCards, it => it === 0), [id]))
      }
    }
  }

  function getCardTheme(id: number) {
    if (selectedCards.includes(id)) {
      return 'dark'
    } else {
      return 'light'
    }
  }

  console.log(languageStudents)
  return <Container>
    <div className={styles.languageStudentAggregateContainer}>
      <div className={`${styles.languageStudentCard} ${styles.languageStudent1}`}>
        {languageStudents.filter(it => it.key == 'T1').map(it =>
          <CardC44 key={it.key} title={it.languageStudentTitle}
            stat={it.languageStudentAggregate.toString()} />)}
      </div>
      <div className={`${styles.languageStudentCard} ${styles.languageStudent2}`}>
        {languageStudents.filter(it => it.key == 'G1').map(it =>
          <CardC44 key={it.key} title={it.languageStudentTitle}
            stat={it.languageStudentAggregate.toString()} />)}
      </div>
      <div className={`${styles.languageStudentCard} ${styles.languageStudent3}`}>
        {languageStudents.filter(it => it.key == 'G2').map(it =>
          <CardC44 key={it.key} title={it.languageStudentTitle}
            stat={it.languageStudentAggregate.toString()} />)}
      </div>
      <div className={`${styles.languageStudentCard} ${styles.languageStudent4}`}>
        {languageStudents.filter(it => it.key == 'G3').map(it =>
          <CardC44 key={it.key} title={it.languageStudentTitle}
            stat={it.languageStudentAggregate.toString()} />)}
      </div>
      <div className={`${styles.languageStudentCard} ${styles.languageStudent5}`}>
        <CardC89 data={languageStudents}></CardC89>
      </div>
      <div className={`${styles.languageStudentCard} ${styles.languageStudent6}`}>

      </div>
      <div className={`${styles.languageStudentCard} ${styles.languageStudent7}`}>
      </div>
      <div className={`${styles.languageStudentCard} ${styles.languageStudent8}`}>
      </div>
      <div className={`${styles.languageStudentCard} ${styles.languageStudent9}`}>
      </div>
      <div className={`${styles.languageStudentCard} ${styles.languageStudent10}`}>
      </div>
      {/*{data.map((it, index) => {*/}
      {/*  return <>*/}
      {/*    <Card className={styles.card} onClick={() => handleClick(index)} data-bs-theme={getCardTheme(index)} >*/}
      {/*      /!*<DropdownButton id='dropdown-basic-button' title={<Image src='menu_dots.png' height='20' width='20' /> }*!/*/}
      {/*      /!*  style={{ position: 'relative', float: 'right', margin: '4px 8px' }}*!/*/}
      {/*      /!*  variant='outline-light'*!/*/}
      {/*      /!*>*!/*/}
      {/*      /!*  <Dropdown.Item href='#/action-1'>Action</Dropdown.Item>*!/*/}
      {/*      /!*  <Dropdown.Item href='#/action-2'>Another action</Dropdown.Item>*!/*/}
      {/*      /!*  <Dropdown.Item href='#/action-3'>Something else</Dropdown.Item>*!/*/}
      {/*      /!*  <DropdownDivider />*!/*/}
      {/*      /!*  <Dropdown.Item href='#/action-1'>Select/Unselect</Dropdown.Item>*!/*/}
      {/*      /!*  <Dropdown.Item href='#/action-2'>Another action</Dropdown.Item>*!/*/}
      {/*      /!*  <Dropdown.Item href='#/action-3'>Something else</Dropdown.Item>*!/*/}
      {/*      /!*</DropdownButton>*!/*/}
      {/*      <Card.Body>*/}
      {/*        <Card.Text className='h6'>{it.languageStudent_title}</Card.Text>*/}
      {/*        <Card.Text className='' style={{fontFamily:'courier'} }>*/}
      {/*          {it.languageStudent_aggregate}*/}
      {/*        </Card.Text>*/}
      {/*      </Card.Body>*/}
      {/*    </Card>*/}
      {/*  </>*/}
      {/*})}*/}
    </div>
    {languageStudents.map(it => <div>
      {it.languageStudentTitle}
    </div>)}
  </Container>
}

export default DashboardDb4