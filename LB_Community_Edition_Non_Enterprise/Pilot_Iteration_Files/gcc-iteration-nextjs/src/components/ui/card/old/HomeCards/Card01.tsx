import { Card, CardFooter, Image, Button, CardBody } from '@nextui-org/react'

function Card01() {
  return (
    <Card
      isFooterBlurred
      className="border-none"
      radius="lg"
      style={{ width: '18rem' }}
    >
      <Image
        alt="Woman listing to music"
        className="object-cover"
        height={200}
        src="/demo_06.png"
        width={200}
      />
      <CardBody>
        Powerschool Mtss & RTI Scheduler
        <div>
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </div>
      </CardBody>
      <CardFooter className="justify-between before:bg-white/10 border-white/20 border-1 overflow-hidden py-1 absolute before:rounded-xl rounded-large bottom-1 w-[calc(100%_-_8px)] shadow-small ml-1 z-10">
        <p className="text-tiny text-white/80">Available soon.</p>
        <Button
          className="text-tiny text-white bg-black/20"
          color="default"
          radius="lg"
          size="sm"
          variant="flat"
        >
          Notify me
        </Button>
        <ListGroup className="list-group-flush">
          <ListGroup.Item>Cras justo odio</ListGroup.Item>
          <ListGroup.Item>Dapibus ac facilisis in</ListGroup.Item>
          <ListGroup.Item>Vestibulum at eros</ListGroup.Item>
        </ListGroup>
        <Card.Body>
          <Card.Link href="#">Card Link</Card.Link>
          <Card.Link href="#">Another Link</Card.Link>
        </Card.Body>
      </CardFooter>
    </Card>
  )
}

export default Card01
