using System.Net.Mime;
using lb_frontend_02.Server.Controllers.API_v1.StudentPage;
using Microsoft.AspNetCore.Mvc;
using Microsoft.IdentityModel.Tokens;

namespace lb_frontend_02.Server.Controllers.API_v1.DashboardPage;

[Produces(MediaTypeNames.Application.Json)]
[Route("api/v1/dashboard/[controller]/{org}")]
public class D81Controller(
    ILogger<D81Controller> logger,
    ApplicationDbContext context) : DashboardControllerBase
{
    [HttpGet("", Name = "GetD81")]
    public D81Page Get(int org, [FromQuery] string? filter)
    {
        if (filter.IsNullOrEmpty())
            using (context)
            {
                var data = DashboardQueries.GetD81Aggregators(DashboardUtils.CreateAnalyticAggregators(),
                    DashboardUtils.CreateDemographicsAggregators(), org, context);
                return data;
            }

        using (context)
        {
            var data = DashboardQueries.GetD81AggregatorsWithFilter(DashboardUtils.CreateAnalyticAggregators(),
                DashboardUtils.CreateDemographicsAggregators(), org, context, filter!);
            return data;
        }
    }

    [HttpGet("students/{pageTake:int}/{pageSkip:int}/{sort}", Name = "GetD81Students")]
    public D81Table GetStudents(int org, string? sort, int? pageSkip, int pageTake, [FromQuery] string? filter)
    {
        using (context)
        {
            var students = new List<DashboardStudentDetailed>();
            IQueryable<Student> studentsQuery =
                from student
                    in context.Students
                where student.Org!.OrgId == org
                select student;
            var studentsArray = studentsQuery.Take(pageTake).ToArray();
            for (var i = 0; i < studentsArray.Length; i++)
                students.Add(new DashboardStudentDetailed
                {
                    Key = students[i].Key
                });

            return new D81Table
            {
                Students = students
            };
        }
    }
}