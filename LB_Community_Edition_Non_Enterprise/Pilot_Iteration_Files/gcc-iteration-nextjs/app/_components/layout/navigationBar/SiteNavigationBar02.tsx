import { Navbar, NavbarBrand, NavbarContent, NavbarItem } from "@nextui-org/navbar";
import { Button } from "@nextui-org/button";
import Image from "next/image";

export default function SiteNavigationBar02() {
    return <Navbar isBordered>
        <NavbarBrand>
            <Image src="/logo.svg" alt="Learning Blocks" width={120} height={40}/>
            <div style={{display: 'flex', flexGrow: 1}}><Image
                style={{marginLeft: 16, marginRight: 16}} src="/menu_point_filled_dark.svg" alt="Menu indicator"
                height={24}
                width={24}/><span>Northstop Unified School District</span>
            </div>
        </NavbarBrand>
        <NavbarContent justify="end">
            <NavbarItem className="hidden lg:flex">
                <Button radius="full" className="bg-gradient-to-tr from-pink-500 to-yellow-500 text-white shadow-lg">
                    Login
                </Button>
            </NavbarItem>
        </NavbarContent>
    </Navbar>
}
