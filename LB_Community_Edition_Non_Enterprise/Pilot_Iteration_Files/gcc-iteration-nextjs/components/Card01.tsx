'use client'; // Ensures this component is rendered on the client side

import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';

function Card01() {
  return (
    <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src="/demo_03.png" />
      <Card.Body>
        <Card.Title>Powerschool Mtss & RTI Scheduler</Card.Title>
        <Card.Text>
          Some quick example text to build on the card title and make up the
          bulk of the card's content. zzxcsasda
        </Card.Text>
      </Card.Body>
      <ListGroup className="list-group-flush">
        <ListGroup.Item>Cras justo odio</ListGroup.Item>
        <ListGroup.Item>Dapibus ac facilisis in</ListGroup.Item>
        <ListGroup.Item>Vestibulum at eros</ListGroup.Item>
      </ListGroup>
      <Card.Body>
        <Card.Link href="#">Card Link</Card.Link>
        <Card.Link href="#">Another Link</Card.Link>
      </Card.Body>
    </Card>
  );
}

export default Card01;
