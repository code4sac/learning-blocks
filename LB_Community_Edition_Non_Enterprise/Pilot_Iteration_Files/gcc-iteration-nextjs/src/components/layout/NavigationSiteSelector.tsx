'use client'

interface NavigationSiteSelectorProps {
  sites: string[]
  selectedSite?: string
  onSiteSelect: (site: string) => void
}

const NavigationSiteSelector: React.FC<NavigationSiteSelectorProps> = ({
  sites,
  selectedSite,
  onSiteSelect,
}) => {
  return (
    <div className="navigation-site-selector">
      {/* <div style={{ display: 'flex', flexGrow: 1 }}>
        <Image
          style={{ marginLeft: 16, marginRight: 16 }}
          src="/menu_point_filled_dark.svg"
          alt="Menu indicator"
          height={24}
          width={24}
        />
        <span>GCC Pilot Iteration</span>
      </div> */}
      <select
        value={selectedSite ? selectedSite : sites[0]}
        onChange={(e) => onSiteSelect(e.target.value)}
      >
        {sites.map((site) => (
          <option key={site} value={site}>
            {site}
          </option>
        ))}
      </select>
    </div>
  )
}

export default NavigationSiteSelector
