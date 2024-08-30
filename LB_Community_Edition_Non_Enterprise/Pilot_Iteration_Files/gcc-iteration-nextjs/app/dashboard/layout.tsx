import SiteNavigationBar from "../_components/layout/navigationBar/SiteNavigationBar02";

export default function Layout({ children }) {
  return (
    <div>
      <SiteNavigationBar loggedIn={false}></SiteNavigationBar>
      <div>{children}</div>
    </div>
  );
}
