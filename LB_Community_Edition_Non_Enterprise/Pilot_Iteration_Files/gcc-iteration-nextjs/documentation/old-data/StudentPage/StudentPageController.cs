using System.Net.Mime;
using lb_frontend_02.Server.Controllers.API_v1.DashboardPage;
using Microsoft.AspNetCore.Mvc;

namespace lb_frontend_02.Server.Controllers.API_v1.StudentPage;

[Produces(MediaTypeNames.Application.Json)]
[Route("api/v1/dashboard/[controller]")]
public class StudentPageController(ILogger<DemographicsDashboardPageController> logger, ApplicationDbContext context)
    : DashboardControllerBase
{
    [HttpGet("{org}", Name = "GetStudentPage")]
    public IEnumerable<DashboardDemographicAggregate> Get(int org, [FromQuery] string? filter)
    {
        using (context)
        {
            return DashboardQueries.GetDemographicAggregators(DashboardUtils.CreateDemographicsAggregators(), org,
                context);
        }
    }
}