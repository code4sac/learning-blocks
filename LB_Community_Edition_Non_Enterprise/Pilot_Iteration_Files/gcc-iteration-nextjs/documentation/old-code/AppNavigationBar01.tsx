'use client'
import { useState } from 'react'
import {
  Container,
  Dropdown,
  Form,
  InputGroup,
  Nav,
  Navbar,
} from 'react-bootstrap'
import links from '../../__tests__/mock/links01.json'
import styles from './AppNavigationBar01.module.css'
import { SubMenu } from '@/utilities/models/page'
import Image from 'next/image'

interface NEAppNavigationBarProps {
  selectedMenu: string
  selectedSubMenu: SubMenu
  onClickSubMenuLink: any
}

/**
 * Non-enterprise app navigation bar.
 * @param subMenu {string} The selected toolbar menu.
 * @returns App container child element.
 */
function AppNavigationBar01({
  onClickSubMenuLink,
  selectedMenu,
  selectedSubMenu,
}: NEAppNavigationBarProps) {
  const [querySaveDisabled, setQuerySaveDisabled] = useState(false)

  function capitalizeFirstLetter(text: string) {
    return text.charAt(0).toUpperCase() + text.slice(1)
  }

  return (
    <div className={`${styles.mainToolbarContainer}`}>
      <Navbar className={`justify-content-between border-bottom`}>
        <Container>
          <Nav>
            {links.map((link) => {
              return (
                <div key={link.key}>
                  <a
                    href={link.key}
                    className={`${styles.menuLink} ${
                      link.key === selectedMenu ? styles.menuLinkSelected : ''
                    }`}
                  >
                    <Image
                      src={
                        link.key === selectedMenu
                          ? `${link.menuIcon}_light.svg`
                          : `${link.menuIcon}.svg`
                      }
                      width="24"
                      height="24"
                      alt="Expand navbar"
                    />
                    <span style={{ paddingLeft: '4px', fontWeight: '600' }}>
                      {capitalizeFirstLetter(link.key)}
                    </span>
                  </a>
                </div>
              )
            })}
          </Nav>
          <Nav>
            <Dropdown style={{ display: 'inline-block' }}>
              <Dropdown.Toggle
                id="dropdown-basic"
                className="bg-transparent"
                style={{ border: 0, color: 'black' }}
              >
                New Query 1*
              </Dropdown.Toggle>

              <Dropdown.Menu>
                <Dropdown.Item onClick={() => null} href="" disabled={true}>
                  New Query 1*
                </Dropdown.Item>
                <Dropdown.Item href="">View All (0)</Dropdown.Item>
                <Dropdown.Divider />
                <Dropdown.Item href="" onClick={() => null}>
                  Save
                </Dropdown.Item>
                <Dropdown.Item href="" onClick={() => null}>
                  Rename
                </Dropdown.Item>
                {selectedMenu !== 'dashboard' ? (
                  <Dropdown.Item href="" onClick={() => null}>
                    View Dashboard
                  </Dropdown.Item>
                ) : null}
              </Dropdown.Menu>
              {selectedMenu === 'dashboard' ? (
                <button disabled={querySaveDisabled}>Save</button>
              ) : null}
            </Dropdown>
          </Nav>
          <Nav>
            <Form>
              <InputGroup>
                <InputGroup.Text id="basic-addon1">
                  <Image
                    src="/menu_search.png"
                    alt="Search"
                    height="20"
                    width="20"
                  />
                </InputGroup.Text>
                <Form.Control
                  placeholder="Search"
                  aria-label="Search"
                  aria-describedby="basic-addon1"
                />
              </InputGroup>
            </Form>
          </Nav>
        </Container>
      </Navbar>
    </div>
  )
}

export default AppNavigationBar01
