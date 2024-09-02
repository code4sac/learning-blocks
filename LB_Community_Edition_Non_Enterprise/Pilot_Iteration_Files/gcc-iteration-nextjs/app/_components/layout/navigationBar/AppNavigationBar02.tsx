import links from "@/__tests__/mock/links01.json";
import styles from "./AppNavigationBar01.module.css";
import { SubMenu } from "@/app/_utilities/models/page";
import Image from "next/image";
import { useState } from "react";
import { Container, Form, InputGroup, Nav, Navbar } from "react-bootstrap";

interface NEAppNavigationBarProps {
  selectedMenu: string;
  selectedSubMenu: SubMenu;
  onClickSubMenuLink: any;
}

/**
 * Non-enterprise app navigation bar.
 * @param subMenu {string} The selected toolbar menu.
 * @returns App container child element.
 */
function AppNavigationBar02({
  onClickSubMenuLink,
  selectedMenu,
  selectedSubMenu,
}: NEAppNavigationBarProps) {
  const [querySaveDisabled, setQuerySaveDisabled] = useState(false);

  function capitalizeFirstLetter(text: string) {
    return text.charAt(0).toUpperCase() + text.slice(1);
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
                      link.key === selectedMenu ? styles.menuLinkSelected : ""
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
                    <span style={{ paddingLeft: "4px", fontWeight: "600" }}>
                      {capitalizeFirstLetter(link.key)}
                    </span>
                  </a>
                </div>
              );
            })}
          </Nav>
          <Nav>
            <Form>
              <InputGroup>
                <InputGroup.Text id="basic-addon1">
                  <Image src="/menu_search.png" alt="Search" />
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
  );
}

export default AppNavigationBar02;
