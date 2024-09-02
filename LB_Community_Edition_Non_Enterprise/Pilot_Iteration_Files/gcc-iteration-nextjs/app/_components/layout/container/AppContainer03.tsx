interface NEAppContainerProps {
  selectedMenu: string;
  selectedSubMenu: string;
  setCurrentSubMenu: any;
  children: any;
}

/**
 * Enterprise app container.
 * @param children {ReactElement} Content for the inner application.
 * @param selectedMenu {string} The .
 * @param selectedSubMenu {string} The .
 * @param setCurrentSubMenu {any} The .
 * @returns App container child element.
 */
export default async function AppContainer03({
  children,
  selectedMenu,
  selectedSubMenu,
  setCurrentSubMenu,
}: NEAppContainerProps) {
  return (
    <div>
      <h1>a</h1>
      <div>{children}</div>
    </div>
  );
}
