import Container from 'react-bootstrap/Container';
import Image from 'next/image';

function AppNavBar() {
  return (
    <>
      <Container>

        <div>
          <span style={{ float: 'right' }}><Image src="/icon_info.svg" alt="info" /> Learning Blocks Enterprise Demo v0.0.1-microsoft-azure.1</span>
        </div>
      </Container>
    </>
  );
}

export default AppNavBar;