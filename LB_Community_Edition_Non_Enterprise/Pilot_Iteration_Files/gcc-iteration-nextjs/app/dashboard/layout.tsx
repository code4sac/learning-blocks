import SiteNavigationBar02 from "@/app/_components/layout/navigationBar/SiteNavigationBar02";

export default function Layout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <div>
      <SiteNavigationBar02></SiteNavigationBar02>
      <div>{children}</div>
    </div>
  );
}
