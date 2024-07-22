export interface NEAppInnerContentProps {
  children: any
}

/**
 * Main application content.
 * @param children {any} The .
 * @returns App container child element.
 */
function AppInnerContent({children}: NEAppInnerContentProps) {
  return <div>
    {children}
  </div>
}

export default AppInnerContent