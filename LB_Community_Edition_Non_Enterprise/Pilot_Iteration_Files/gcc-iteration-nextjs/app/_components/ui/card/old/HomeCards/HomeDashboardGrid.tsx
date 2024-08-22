import Card03 from "./Card03";
import styles from "./HomeDashboardGrid.module.css"

function HomeDashboardGrid() {
    return (<>
        <h2 className={styles.dashboard_header}>Northstop Unified School District Dashboards</h2>
        <div className={'home_dashboard_list_container'}>
            <Card03></Card03>
        </div>
    </>);
}

export default HomeDashboardGrid;
