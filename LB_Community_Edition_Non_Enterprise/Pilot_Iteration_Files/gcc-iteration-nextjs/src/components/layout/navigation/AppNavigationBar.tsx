import links from '../../../../__tests__/mock/links01.json'
import styles from './AppNavigationBar.module.css'
import { SubMenu } from '@/utility/models/page'
import Image from 'next/image'
import { useState } from 'react'
import {
  Button,
  Input,
  Navbar,
  NavbarContent,
  NavbarItem,
} from '@nextui-org/react'
import { SearchIcon } from './SearchIcon'

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
function AppNavigationBar({
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
        <div>
          <NavbarContent justify="end">
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
            <NavbarItem className="hidden lg:flex"></NavbarItem>
            <NavbarItem>
              <Input
                label="Search"
                isClearable
                radius="lg"
                classNames={{
                  label: 'text-black/50 dark:text-white/90',
                  input: [
                    'bg-transparent',
                    'text-black/90 dark:text-white/90',
                    'placeholder:text-default-700/50 dark:placeholder:text-white/60',
                  ],
                  innerWrapper: 'bg-transparent',
                  inputWrapper: [
                    'shadow-xl',
                    'bg-default-200/50',
                    'dark:bg-default/60',
                    'backdrop-blur-xl',
                    'backdrop-saturate-200',
                    'hover:bg-default-200/70',
                    'dark:hover:bg-default/70',
                    'group-data-[focus=true]:bg-default-200/50',
                    'dark:group-data-[focus=true]:bg-default/60',
                    '!cursor-text',
                  ],
                }}
                placeholder="Type to search..."
                startContent={
                  <SearchIcon className="text-black/50 mb-0.5 dark:text-white/90 text-slate-400 pointer-events-none flex-shrink-0" />
                }
              />
            </NavbarItem>
          </NavbarContent>
        </div>
      </Navbar>
    </div>
  )
}

export default AppNavigationBar
