using System.Net.Mime;
using Microsoft.AspNetCore.Mvc;

namespace lb_frontend_02.Server.Controllers.API_v1.DashboardPage;

[Produces(MediaTypeNames.Application.Json)]
[Route("api/v1/dashboard/[controller]")]
public class DemographicsDashboardPageController(
    ILogger<DemographicsDashboardPageController> logger,
    ApplicationDbContext context) : DashboardControllerBase
{
    [HttpGet("{org}", Name = "GetDashboardDemographicAggregate")]
    public IEnumerable<DashboardDemographicAggregate> Get(int org, [FromQuery] string? filter)
    {
        using (context)
        {
            return DashboardQueries.GetDemographicAggregators(DashboardUtils.CreateDemographicsAggregators(), org,
                context);
        }
    }
}