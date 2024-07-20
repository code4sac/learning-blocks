import Card01 from "./Card01";
import Card03 from "./Card03";
import Card02 from "./Card02";
import Card04 from "./Card04";
import { Link } from "@tanstack/react-router";

function HomeDashboardGrid() {
  return (<>
    <h2>GCC Dashboards</h2>
    <div className={'home_dashboard_list_container'}>
      <Link to="/dashboard01"><Card01 /></Link>
      <Link to="/dashboard02"><Card02 /></Link>
      <Link to="/dashboard03"><Card03 /></Link>
      <Link to="/dashboard04"><Card04 /></Link>
    </div>
  </>);
}

export default HomeDashboardGrid;
