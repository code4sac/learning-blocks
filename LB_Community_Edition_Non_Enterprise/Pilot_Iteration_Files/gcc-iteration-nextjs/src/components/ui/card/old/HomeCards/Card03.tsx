import { Link } from '@tanstack/react-router'
import Card from 'react-bootstrap/Card'
import ListGroup from 'react-bootstrap/ListGroup'

function Card03() {
  return (
    <Card style={{ width: '18rem' }}>
      <Link to="/dashboard03">
        <Card.Img src="/demo_03.png" variant="top" />
      </Link>
      <Card.Body>
        <Link to="/dashboard03">
          <Card.Title>Demographic Aggregate</Card.Title>
        </Link>
        <Card.Text>
          Search and filter data by school demographic data.
        </Card.Text>
      </Card.Body>
      <ListGroup className="list-group-flush">
        <ListGroup.Item>
          <Link to="/dashboard03">Intervention analytics</Link>
        </ListGroup.Item>
      </ListGroup>
    </Card>
  )
}

export default Card03
