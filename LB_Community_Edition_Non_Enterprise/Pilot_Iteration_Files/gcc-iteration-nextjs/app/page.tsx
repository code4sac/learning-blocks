import styles from './page.module.css'; // Ensure this path is correct
import Card01 from '@/components2/Card01'; // Import the Card01 component

export default function Home() {
  return (
    <main className={styles.main}>


      <Card01/>

    </main>
  );
}
