'use-client'

import Image from 'next/image'
import { Input, Navbar, NavbarContent, NavbarItem } from '@nextui-org/react'
import Link from 'next/link'
import { capitalize } from 'lodash'

import { SubMenu } from '@/utility/models/page'

import links from '../../../__tests__/mock/links01.json'

import styles from './AppNavigationBar.module.css'
import { SearchIcon } from '@/utility/Icons'

interface AppNavigationBarProps {
  selectedMenu: string
  selectedSubMenu: SubMenu
  onClickSubMenuLink: any
}

/**
 * App navigation bar. Old props: onClickSubMenuLink, selectedSubMenu
 */
function AppNavigationBar({ selectedMenu }: AppNavigationBarProps) {
  return (
    <div className={`${styles.mainToolbarContainer}`}>
      <Navbar className={`border-bottom`}>
        <NavbarContent justify="start">
          {links.map((link) => {
            return (
              <div key={link.key}>
                <Link
                  className={`${styles.menuLink} ${
                    link.key === selectedMenu && styles.menuLinkSelected
                  }`}
                  href={link.key}
                >
                  <Image
                    alt=""
                    height="24"
                    src={
                      link.key === selectedMenu
                        ? `/${link.menuIcon}_light.svg`
                        : `/${link.menuIcon}.svg`
                    }
                    width="24"
                  />
                  <span style={{ paddingLeft: '4px', fontWeight: '600' }}>
                    {capitalize(link.key)}
                  </span>
                </Link>
              </div>
            )
          })}
        </NavbarContent>
        <NavbarContent justify="end">
          <NavbarItem>
            <Input
              isClearable
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
              label="Search"
              placeholder="Type to search..."
              radius="lg"
              startContent={
                <SearchIcon className="text-black/50 mb-0.5 dark:text-white/90 text-slate-400 pointer-events-none flex-shrink-0" />
              }
            />
          </NavbarItem>
        </NavbarContent>
      </Navbar>
    </div>
  )
}

export default AppNavigationBar
