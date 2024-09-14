import { Navbar, NavbarContent, NavbarItem } from '@nextui-org/react'

export function SiteFooter() {
  return (
    <Navbar className="font-semibold">
      <NavbarContent justify="start">
        <NavbarItem>Terms of Use</NavbarItem>
        <NavbarItem>Privacy Policy</NavbarItem>
        <NavbarItem>HIPPA</NavbarItem>
      </NavbarContent>
      <NavbarContent justify="end">
        <NavbarItem>2024 © Open Sacramento</NavbarItem>
      </NavbarContent>
    </Navbar>
  )
}

export default SiteFooter
