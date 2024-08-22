import Link from 'next/link';
import styles from './page.module.css'; // Ensure this path is correct

let context = {
    auth: undefined!,
    navigationKey: 'example 01',
    queryKey: '1efa02',
}

export default function Home() {
    return (
        <main className={styles.main}>

            {/* <DashboardPage navigationKey={context.navigationKey} queryKey={context.queryKey}></DashboardPage> */}

            {/* <DashboardPage navigationKey={context.navigationKey} queryKey={context.queryKey} /> */}

            <div>Landing Page</div>

            <Link href="/dashboard">Dashboard</Link>

        </main>
    );
}


/**
 * Handle app logic and render the inner app content.
 * @see renderInnerContent [Page component documentation](components/pages/README.md#arenderInnerContent)
 * @returns App container child element.
 */
// function renderInnerContent(): ReactElement {
//   switch (currentSubMenu) {
//     case SubMenu.Example01:
//       return <DashboardManager data={data} selectedSubMenu={currentSubMenu}
//         setPageQueryKey={setPageQueryKey}></DashboardManager>
//     case SubMenu.Example02:
//       return <DashboardManager data={data} selectedSubMenu={currentSubMenu}></DashboardManager>
//     default:
//       return <DashboardManager data={data} selectedSubMenu={SubMenu.Example01}></DashboardManager>
//   }
// }