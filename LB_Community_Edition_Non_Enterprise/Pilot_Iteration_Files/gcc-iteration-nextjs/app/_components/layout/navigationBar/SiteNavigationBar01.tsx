"use client";
import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";
import Dropdown from "react-bootstrap/Dropdown";
import Image from "next/image";
import Offcanvas from "react-bootstrap/Offcanvas";
import { useState } from "react";
import styles from "./SiteNavigationBar01.module.css";

function signOut() {
  localStorage.clear();
  window.location.href = "/login";
}

function SiteNavigationBar01(loggedIn) {
  const [showSidebar, setShowSidebar] = useState(false);
  const handleClose = () => setShowSidebar(false);
  const handleShow = () => setShowSidebar(true);
  const [showAccessibilityOptions, setShowAccessibilityOptions] =
    useState(false);

  return (
    <div>
      <Offcanvas show={showSidebar} onHide={handleClose} placement="end">
        <Offcanvas.Header closeButton>
          <Offcanvas.Title>Language</Offcanvas.Title>
        </Offcanvas.Header>
        <Offcanvas.Body>
          <form action="/action_page.php">
            <p>Select your language:</p>
            <input type="radio" id="age1" name="age" value="30" checked />
            <label for="age1">English</label>
            <br />
            <input type="radio" id="age2" name="age" value="60" />
            <label for="age2">Español</label>
            <br />
            <input type="radio" id="age3" name="age" value="100" />
            <label for="age3">简体中文</label>
            <br />
            <br />
          </form>
        </Offcanvas.Body>
      </Offcanvas>
      {showAccessibilityOptions ? <Navbar>Accessibility Options</Navbar> : null}
      <div
        style={
          loggedIn.loggedIn
            ? { background: "#850A0A" }
            : { background: "#FFFFFF" }
        }
        className={`${styles.mainToolbarContainer}`}
      >
        <Container>
          <div className={`${styles.innerToolbarContainer}`}>
            <a href={"/"}>
              <Image
                width={148}
                height={60}
                src={loggedIn.loggedIn ? "/logosvg" : "/logo.svg"}
                className=""
                alt="Learning Blocks logo"
              />
            </a>
            <div style={{ display: "flex", flexGrow: 1, color: "white" }}>
              <Image
                style={{ marginLeft: 16, marginRight: 16 }}
                src="/menu_point_filled_light.svg"
                alt="Menu indicator"
                height={24}
                width={24}
              />
              <span
                style={{ fontWeight: 600, size: "16px", lineHeight: "20px" }}
              >
                Northstop Unified School District
              </span>
            </div>
            <div>
              <div className={`${styles.mainToolbarIconsContainer}`}>
                <span
                  onClick={() =>
                    setShowAccessibilityOptions(!showAccessibilityOptions)
                  }
                >
                  <Image
                    width={148}
                    height={60}
                    src={
                      loggedIn.loggedIn
                        ? "/menu_accessible.png"
                        : "/menuAccessibleImage"
                    }
                    alt="Help / Support"
                  />
                </span>
                <span onClick={() => setShowSidebar(true)}>
                  <Image
                    width={148}
                    height={60}
                    src={
                      loggedIn.loggedIn
                        ? "/menu_world.png"
                        : "/menu_world_light.png"
                    }
                    alt="Help / Support"
                  />
                </span>
                <a href="/support">
                  <Image
                    width={148}
                    height={60}
                    src={
                      loggedIn.loggedIn
                        ? "/menu_help_circle.png"
                        : "/menu_help_circle_light.png"
                    }
                    alt="Help / Support"
                  />
                </a>
              </div>
              {loggedIn.loggedIn ? (
                <Dropdown style={{ display: "inline-block" }}>
                  <Dropdown.Toggle
                    id="dropdown-basic"
                    className="bg-transparent"
                    style={{ border: 0 }}
                  >
                    Hephaestus Admin
                  </Dropdown.Toggle>

                  <Dropdown.Menu>
                    <Dropdown.Item
                      onClick={() =>
                        setShowAccessibilityOptions(!showAccessibilityOptions)
                      }
                      href=""
                    >
                      Accessibility Options
                    </Dropdown.Item>
                    <Dropdown.Item
                      onClick={() => setShowSidebar(true)}
                      href="#language"
                    >
                      Language
                    </Dropdown.Item>
                    <Dropdown.Item href="/support">Help</Dropdown.Item>
                    <Dropdown.Divider />
                    <Dropdown.Item href="/api/docs">
                      API Documentation
                    </Dropdown.Item>
                    <Dropdown.Item href="/settings">Settings</Dropdown.Item>
                    <Dropdown.Item href="" onClick={signOut}>
                      Sign Out
                    </Dropdown.Item>
                  </Dropdown.Menu>
                </Dropdown>
              ) : null}
            </div>
          </div>
        </Container>
      </div>
    </div>
  );
}

export default SiteNavigationBar;
