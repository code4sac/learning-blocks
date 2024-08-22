export interface DashboardStatisticProps {
    title: string
    stat: string
}

function CardC44({title, stat}: DashboardStatisticProps) {
    return <div style={{padding: '8px'}}>
        <div style={{fontSize: '12px', opacity: '60%', fontWeight: 600}}>{title}</div>
        <div style={{fontSize: '24px', fontWeight: 600}}>{stat}</div>
    </div>
}

export default CardC44