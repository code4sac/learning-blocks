import { Button, Container } from 'react-bootstrap'
import SiteNavigationBar from '../components/app/SiteNavigationBar'
import Footer from '../components/app/SiteFooter'
import logoBlack from '../../public/logo_lb_black_02.png'
import Image from "next/image";

/**
 * Not found page.
 * @returns JSX element.
 */
function NotFoundPage() {
    let element = <div>
        <SiteNavigationBar loggedIn={false}/>
        <Container style={{padding: '60px 0'}}>
            <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center'}}>
                <div>
                    <Image src={logoBlack} alt="Learning Blocks logo"/>
                </div>
                <div style={{fontWeight: 600, fontSize: '2em', lineHeight: '56px'}}>
                    404 Page Not Found
                </div>
                <div style={{fontWeight: 600, lineHeight: '56px'}}>
                    Oops! We can't find that page.
                </div>
                <div>
                    <Button href="/login">Sign In</Button>
                </div>
            </div>
        </Container>
        <Footer></Footer>
    </div>

    return element
}

export default NotFoundPage