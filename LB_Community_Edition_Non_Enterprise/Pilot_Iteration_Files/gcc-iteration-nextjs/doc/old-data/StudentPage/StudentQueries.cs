using lb_frontend_02.Server.Controllers.API_v1.DashboardPage;

namespace lb_frontend_02.Server.Controllers.API_v1.StudentPage;

public class StudentQueries
{
    public static IEnumerable<DashboardDemographicAggregate> Aggregators(
        IEnumerable<DashboardDemographicAggregate> aggregate1, int org, ApplicationDbContext context)
    {
        //IQueryable<Student> studentsQuery = from student in context.Students where student.Org!.OrgId && filterStudent(student, filter) == org select student;
        IQueryable<Student> studentsQuery =
            from student in context.Students
            where student.Org!.OrgId == org
            select student;
        foreach (var student in studentsQuery)
        foreach (var item in aggregate1)
        {
            if (item.Key!.Contains($"R{student.RaceCode1!}") || DashboardUtils.ParseGender(item, student))
                item.DemographicAggregate++;

            if (item.Key!.Equals("T1")) item.DemographicAggregate++;
        }

        // if (!string.IsNullOrEmpty(filter))
        // {
        // }
        // else
        // {
        // }
        return aggregate1;
    }
}