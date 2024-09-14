'use client'

import React from 'react'
import {
  Navbar,
  NavbarBrand,
  NavbarContent,
  NavbarItem,
  Link,
  DropdownItem,
  DropdownTrigger,
  Dropdown,
  DropdownMenu,
  NavbarMenu,
  NavbarMenuItem,
  Button,
  Image,
  NavbarMenuToggle,
} from '@nextui-org/react'

import ProfileDropdown from '@/components/ui/dropdown/ProfileDropdown'
import SiteNavMenuDropdown from '@/components/ui/dropdown/SiteNavMenuDropdown'
import { siteConfig } from '@/utility/constants'

interface SiteNavbarProps {
  loggedIn: boolean
}

export default function SiteNavbar({
  loggedIn: siteSelector,
}: SiteNavbarProps) {
  const menuItems = siteConfig.navMenuItems

  // eslint-disable-next-line no-unused-vars
  const [isMenuOpen, _] = React.useState(false)

  return (
    <Navbar>
      <NavbarContent className="gap-8" justify="start">
        <NavbarMenuToggle
          aria-label={isMenuOpen ? 'Close menu' : 'Open menu'}
          className="sm:hidden"
        />
        <NavbarBrand>
          <Link
            className="visited:text-inherit"
            disableAnimation={true}
            href="/"
          >
            <p className="font-bold text-inherit">Learning Blocks</p>
          </Link>
        </NavbarBrand>
      </NavbarContent>

      {!siteSelector && (
        <NavbarContent className="hidden lg:flex gap-4">
          <NavbarItem>
            <Link color="foreground" href="/app/dashboard">
              Demo
            </Link>
          </NavbarItem>
        </NavbarContent>
      )}

      <NavbarContent as="div" justify="end">
        <NavbarItem className="hidden sm:flex">
          <Image
            alt="Learning Blocks"
            height={24}
            src="/menu_accessible_light.png"
            width={24}
          />
        </NavbarItem>
        <NavbarItem className="hidden sm:flex">
          <Image
            alt="Learning Blocks"
            height={24}
            src="/menu_world_light.png"
            width={24}
          />
        </NavbarItem>
        <NavbarItem className="hidden sm:flex">
          <Image
            alt="Learning Blocks"
            height={24}
            src="/menu_help_circle_light.png"
            width={24}
          />
        </NavbarItem>
        <NavbarItem className="hidden sm:flex">
          {siteSelector ? (
            <ProfileDropdown />
          ) : (
            <Button
              className="bg-gradient-to-tr from-pink-500 to-yellow-500 text-white shadow-lg"
              radius="full"
              as={Link}
              href="/signin"
            >
              Sign In
            </Button>
          )}
        </NavbarItem>
      </NavbarContent>

      <NavbarMenu>
        {menuItems.map((item, index) => (
          <NavbarMenuItem key={`${item}-${index}`}>
            <Link
              className="w-full"
              color={
                index === 2
                  ? 'primary'
                  : index === menuItems.length - 1
                    ? 'danger'
                    : 'foreground'
              }
              href="/app"
              size="lg"
            >
              {item}
            </Link>
          </NavbarMenuItem>
        ))}
      </NavbarMenu>
    </Navbar>
  )
}
