import Container from 'react-bootstrap/Container'

function Footer() {
  return <Container>
    <div>
      <span style={{float: 'left', paddingRight: '16px', fontWeight: '600'}}>Terms of Use</span>
      <span style={{float: 'left', fontWeight: '600'}}>Privacy Policy</span>
      <span style={{float: 'right', fontWeight: '600'}}>Disclaimer</span>
    </div>
  </Container>
}

export default Footer