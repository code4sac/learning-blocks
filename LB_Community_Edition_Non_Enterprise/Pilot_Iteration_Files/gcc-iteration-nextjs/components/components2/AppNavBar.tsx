import { Button } from 'react-bootstrap';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

function AppNavBar() {
  return (
    <Navbar expand="lg" bg="dark" data-bs-theme="dark">
      <Container>
        <Navbar.Brand href="/">Learning Blocks Enterprise</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ms-auto">
            <Nav.Link href="/">Home</Nav.Link>
            <NavDropdown title="Enterprise Features" id="basic-nav-dropdown">
              <NavDropdown.Item href="/docs">API Sync</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">Interventions</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.1">Demographics</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">Analytics</NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item href="#action/3.4">
                Swagger Docs
              </NavDropdown.Item>
              <NavDropdown.Item href="#action/3.4">
                Separated link
              </NavDropdown.Item>
            </NavDropdown>
            <Nav.Link href="/support">Help / Support</Nav.Link>
            <Button><Image src="/icon_person.svg" alt="Navigate to help and support page" /> User</Button>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default AppNavBar;