import styles from './page.module.css'; // Ensure this path is correct
import DashboardPage from '@/components/pages/DashboardPage';

let context = {
  auth: undefined!,
  navigationKey: 'example 01',
  queryKey: '1efa02',
}

export default function Home() {
  return (
    <main className={styles.main}>

      {/* <DashboardPage navigationKey={context.navigationKey} queryKey={context.queryKey}></DashboardPage> */}

      <DashboardPage navigationKey={context.navigationKey} queryKey={context.queryKey} />

    </main>
  );
}
