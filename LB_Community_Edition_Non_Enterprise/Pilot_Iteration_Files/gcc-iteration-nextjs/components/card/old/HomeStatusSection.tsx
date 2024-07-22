import {Button, Col, Row} from "react-bootstrap";

function HomeStatusSection() {
  const a = () => {

  }
  return (<>
    <Row className={'home_section_01_container'}>
      <Col className={'home_section_01_col'}>
        <div className={'home_section_01_api_status'}>
          <Row>
            <h3>System Monitor</h3>
          </Row>
          <Row>
            <p>API not connected.</p>
            <Button onClick={a}>Sync</Button>
          </Row>
          <Row>
            <p>Please see the support page and documentation for help.</p>
          </Row>
        </div>
      </Col>
      <Col className={'home_section_01_col'}>
        <div className={'home_section_01_getting_started'}>
          <ul>
            <li><a
              href="https://github.com/code4sac/learning-blocks/Documentation%20Folder/getting-started.md">Getting
              started with Learning Blocks.</a></li>
            <li><a
              href="https://github.com/code4sac/learning-blocks/Documentation%20Folder/database-management.md">Connect
              to a database (On-premise).</a></li>
            <li><a href="https://github.com/code4sac/learning-blocks/Documentation%20Folder/faq.md">Frequently
              Asked Questions.</a></li>
            <li>To contact support, please visit the support page. <a href="/support">lb-sis.com/support</a>
            </li>
          </ul>
        </div>
      </Col>
    </Row>
  </>);
}

export default HomeStatusSection;