import { Card } from 'react-bootstrap';
import { LoginForm } from './LoginForm';
import styles from './Login.module.css';
import Image from "next/image";

function Login() {
    let a = undefined!

    let element = <div className={styles.loginPageContainer}>
        <Card style={{margin: '64px 0'}} className={`${styles.loginFormContainer} shadow-lg`}>
            <div className={styles.loginFormSectionDescription}>
                <div style={{width: '240px'}}>
                    <div className={'text-heading-h5-bold'}>Sign in as Parent/Student</div>
                    <div className={'text-paragraph-p3-regular'}>Please enter the following information to continue
                    </div>
                </div>
                <div>
                    <Image src="logo_lb_black_02.png" alt="Login" height={20} width={20}/>
                </div>
            </div>
            <div className={`${styles.loginFormSection} ${styles.loginFormSectionDemo}`}>Demo Mode</div>
            <div className={`${styles.loginFormSection} ${styles.loginFormSectionForm}`}>
                <LoginForm updateUser={a}></LoginForm>
            </div>
            <div className={`${styles.loginFormSection} ${styles.loginFormSectionDemo}`}>To proceed to the demo, click
                the submit button.
            </div>
        </Card>
    </div>

    return element
}

export default Login