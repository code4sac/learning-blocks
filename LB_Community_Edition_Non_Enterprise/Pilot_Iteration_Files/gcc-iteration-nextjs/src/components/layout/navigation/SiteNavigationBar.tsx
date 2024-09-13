'use client'
import {
  Navbar,
  NavbarBrand,
  NavbarContent,
  NavbarItem,
} from '@nextui-org/navbar'
import { Button } from '@nextui-org/button'
import Link from 'next/link'
import {
  Dropdown,
  DropdownItem,
  DropdownMenu,
  DropdownTrigger,
  NavbarMenu,
  NavbarMenuItem,
  NavbarMenuToggle,
} from '@nextui-org/react'
import React from 'react'

import { signout } from '@/actions/signout'

import {
  ChevronDown,
  Lock,
  Activity,
  Flash,
  Server,
  TagUser,
  Scale,
} from './Icons'
import NavigationSiteSelector from './NavigationSiteSelector'

function onSiteSelect(site: string) {
  console.log(site)
}

interface SiteNavigationBarProps {
  siteSelector: boolean
}

/**
 * Site navigation bar.
 * Todo (Feature): Add Learning Blocks open source logo.
 * Todo (Optional): Display the current site and implement site selector.
 * @param siteSelector {boolean} Whether to display the site selector.
 * @returns Site navigation bar.
 */
export default function SiteNavigationBar({
  siteSelector,
}: SiteNavigationBarProps) {
  const [isMenuOpen, setIsMenuOpen] = React.useState(false)

  const menuItems = ['Demo', 'Components', 'Login']
  const icons = {
    chevron: <ChevronDown fill="currentColor" size={16} />,
    scale: <Scale className="text-warning" fill="currentColor" size={30} />,
    lock: <Lock className="text-success" fill="currentColor" size={30} />,
    activity: (
      <Activity className="text-secondary" fill="currentColor" size={30} />
    ),
    flash: <Flash className="text-primary" fill="currentColor" size={30} />,
    server: <Server className="text-success" fill="currentColor" size={30} />,
    user: <TagUser className="text-danger" fill="currentColor" size={30} />,
  }
  return (
    <Navbar isBordered>
      <NavbarContent className="gap-8" justify="start">
        <NavbarMenuToggle
          aria-label={isMenuOpen ? 'Close menu' : 'Open menu'}
          className="sm:hidden"
        />
        <NavbarBrand>
          <Link href="/">
            <p className="font-bold text-inherit">Learning Blocks</p>
          </Link>
          {/* <Image src="/logo.svg" alt="Learning Blocks" width={120} height={40} /> */}
          {siteSelector && (
            <NavigationSiteSelector
              sites={['GCC Pilot Iteration']}
              onSiteSelect={onSiteSelect}
            />
          )}
        </NavbarBrand>
      </NavbarContent>

      {!siteSelector && (
        <NavbarContent className="hidden lg:flex gap-4">
          <Dropdown>
            <NavbarItem>
              <DropdownTrigger>
                <Button
                  disableRipple
                  className="p-0 bg-transparent data-[hover=true]:bg-transparent"
                  endContent={icons.chevron}
                  radius="sm"
                  variant="light"
                >
                  Components
                </Button>
              </DropdownTrigger>
            </NavbarItem>
            <DropdownMenu
              aria-label="ACME features"
              className="w-[340px]"
              itemClasses={{
                base: 'gap-4',
              }}
            >
              <DropdownItem
                key="autoscaling"
                description="ACME scales apps to meet user demand, automagically, based on load."
                startContent={icons.scale}
              >
                Autoscaling
              </DropdownItem>
              <DropdownItem
                key="usage_metrics"
                description="Real-time metrics to debug issues. Slow query added? We’ll show you exactly where."
                startContent={icons.activity}
              >
                Usage Metrics
              </DropdownItem>
              <DropdownItem
                key="production_ready"
                description="ACME runs on ACME, join us and others serving requests at web scale."
                startContent={icons.flash}
              >
                Production Ready
              </DropdownItem>
              <DropdownItem
                key="99_uptime"
                description="Applications stay on the grid with high availability and high uptime guarantees."
                startContent={icons.server}
              >
                +99% Uptime
              </DropdownItem>
              <DropdownItem
                key="supreme_support"
                description="Overcome any challenge with a supporting team ready to respond."
                startContent={icons.user}
              >
                +Supreme Support
              </DropdownItem>
            </DropdownMenu>
          </Dropdown>
          <NavbarItem>
            <Link color="foreground" href="/signin">
              Demo
            </Link>
          </NavbarItem>
        </NavbarContent>
      )}

      <NavbarContent justify="end">
        <NavbarItem className="hidden sm:flex">
          {siteSelector ? (
            <Button
              className="bg-gradient-to-tr from-pink-500 to-yellow-500 text-white shadow-lg"
              radius="full"
              onPress={() => signout()}
            >
              Sign Out
            </Button>
          ) : (
            <Button
              className="bg-gradient-to-tr from-pink-500 to-yellow-500 text-white shadow-lg"
              radius="full"
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
              href="#"
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
