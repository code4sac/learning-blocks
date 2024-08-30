import React from "react";
import {
  Navbar,
  NavbarBrand,
  NavbarContent,
  NavbarItem,
} from "@nextui-org/navbar";
import { Button } from "@nextui-org/button";
import { Image } from "@nextui-org/image";

export default function SiteNavigationBar03() {
  return (
    <Navbar isBordered>
      <NavbarBrand>
        <Image src="/logo.svg" alt="Learning Blocks" />
      </NavbarBrand>
      <NavbarContent justify="end">
        <NavbarItem className="hidden lg:flex">
          <Image src="/menu_accessible_light.png" alt="Menu indicator" />
          <Button
            radius="full"
            className="bg-gradient-to-tr from-pink-500 to-yellow-500 text-white shadow-lg"
          >
            Login
          </Button>
        </NavbarItem>
      </NavbarContent>
    </Navbar>
  );
}
