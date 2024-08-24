using System.Linq.Expressions;
using System.Text.RegularExpressions;
using lb_frontend_02.Server.Controllers.API_v1.StudentPage;

namespace lb_frontend_02.Server.Controllers.API_v1.DashboardPage;

public static class DashboardQueries
{
    public static D81Page GetD81Aggregators(
        IEnumerable<DashboardAnalyticAggregate> aggregate01,
        IEnumerable<DashboardDemographicAggregate> aggregate02,
        int org, ApplicationDbContext context)
    {
        //IQueryable<Student> studentsQuery = from student in context.Students where student.Org!.OrgId && filterStudent(student, filter) == org select student;
        IQueryable<Student> studentsQuery =
            from student
                in context.Students
            where student.Org!.OrgId == org
            select student;

        float totalStudents = studentsQuery.Count();

        foreach (var student in studentsQuery)
        {
            foreach (var item in aggregate01) UpdateAggregate(item, student, totalStudents);

            foreach (var item in aggregate02)
            {
                if (item.Key!.Contains($"R{student.RaceCode1!}") || DashboardUtils.ParseGender(item, student))
                    item.DemographicAggregate++;

                if (item.Key!.Equals("T1")) item.DemographicAggregate++;
            }
        }

        //foreach (var item in aggregate01)
        //    item.AnalyticsImage = item.LevelAmount switch
        //    {
        //        <= 20 => "chart_analytics_very_low.png",
        //        <= 40 => "chart_analytics_low.png",
        //        <= 60 => "chart_analytics_medium.png",
        //        <= 80 => "chart_analytics_high.png",
        //        <= 100 => "chart_analytics_very_high.png",
        //        _ => ""
        //    };

        // if (!string.IsNullOrEmpty(filter))
        // {
        // }
        // else
        // {
        // }
        var result = new D81Page
        {
            Analytics = aggregate01,
            Demographics = aggregate02,
            Students = []
        };
        return result;
    }

    private static void UpdateAggregate(DashboardAnalyticAggregate item, Student student, float totalStudents)
    {
        switch (item.Key)
        {
            case "A9e41":
                item.AnalyticLevelAmount += (float)student.ChronicAbsenteeism! / totalStudents;
                item.AnalyticCategories = ParseCategory(student.ChronicAbsenteeism!, item.AnalyticCategories!);
                break;
            case "Aaa59":
                item.AnalyticLevelAmount += (float)student.SuspensionRate! / totalStudents;
                item.AnalyticCategories = ParseCategory(student.SuspensionRate!, item.AnalyticCategories!);
                break;
            case "A4793":
                item.AnalyticLevelAmount += (float)student.GraduationRate! / totalStudents;
                item.AnalyticCategories = ParseCategory(student.GraduationRate!, item.AnalyticCategories!);
                break;
            case "A7924":
                item.AnalyticLevelAmount += (float)student.CollegeAndCareer! / totalStudents;
                item.AnalyticCategories = ParseCategory(student.CollegeAndCareer!, item.AnalyticCategories!);
                break;
            case "A2fcb":
                item.AnalyticLevelAmount += (float)student.UnduplicatedCount! / totalStudents;
                item.AnalyticCategories = ParseCategory(student.UnduplicatedCount!, item.AnalyticCategories!);
                break;
            case "Ae5f9":
                item.AnalyticLevelAmount += (float)student.Ltel! / totalStudents;
                item.AnalyticCategories = ParseCategory(student.Ltel!, item.AnalyticCategories!);
                break;
            case "A418f":
                item.AnalyticLevelAmount += (float)student.ELA! / totalStudents;
                item.AnalyticCategories = ParseCategory(student.ELA!, item.AnalyticCategories!);
                break;
            case "A0d7f":
                item.AnalyticLevelAmount += (float)student.MATH! / totalStudents;
                item.AnalyticCategories = ParseCategory(student.MATH!, item.AnalyticCategories!);
                break;
        }
    }

    private static IEnumerable<DashboardAnalyticCategory> ParseCategory(int? v,
        IEnumerable<DashboardAnalyticCategory> analyticCategories)
    {
        switch (v)
        {
            case <= 20:
                analyticCategories.ElementAt(0).AnalyticCategoryStudentAmount++;
                break;
            case > 20 and <= 40:
                analyticCategories.ElementAt(1).AnalyticCategoryStudentAmount++;
                break;
            case > 40 and <= 60:
                analyticCategories.ElementAt(2).AnalyticCategoryStudentAmount++;
                break;
            case > 60 and <= 80:
                analyticCategories.ElementAt(3).AnalyticCategoryStudentAmount++;
                break;
            case > 80 and <= 100:
                analyticCategories.ElementAt(4).AnalyticCategoryStudentAmount++;
                break;
        }

        return analyticCategories;
        //<= 20 => analyticCategories.ElementAt(0).CategoryAmount++;
        //<= 40 => analyticCategories.ElementAt(1).CategoryAmount++;
        //<= 60 => analyticCategories.ElementAt(2).CategoryAmount++;
        //<= 80 => analyticCategories.ElementAt(3).CategoryAmount++;
        //<= 100 => analyticCategories.ElementAt(4).CategoryAmount++;
        //_ => null;
    }

    public static IEnumerable<DashboardDemographicAggregate> GetDemographicAggregators(
        IEnumerable<DashboardDemographicAggregate> aggregate, int org, ApplicationDbContext context)
    {
        //IQueryable<Student> studentsQuery = from student in context.Students where student.Org!.OrgId && filterStudent(student, filter) == org select student;
        IQueryable<Student> studentsQuery =
            from student in context.Students where student.Org!.OrgId == org select student;
        foreach (var student in studentsQuery)
        foreach (var item in aggregate)
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
        return aggregate;
    }


    private static Expression<Func<Student, bool>> GetSelectXpr(string category, short value)
    {
        if (category == "A9e41")
            return e => e.ChronicAbsenteeism! <= value;
        if (category == "flagged")
            return e => true;
        return e => true;
    }

    public static D81Page GetD81AggregatorsWithFilter(IEnumerable<DashboardAnalyticAggregate> createAnalyticAggregators,
        IEnumerable<DashboardDemographicAggregate> createDemographicsAggregators, int org, ApplicationDbContext context,
        string filter)
    {
        var level = Level(filter);
        IQueryable<Student> studentsQuery =
            from student
                in context.Students
            where student.Org!.OrgId == org && student.ChronicAbsenteeism! <= level
            select student;

        float totalStudents = studentsQuery.Count();
        var dashboardAnalyticAggregates = createAnalyticAggregators as DashboardAnalyticAggregate[] ??
                                          createAnalyticAggregators.ToArray();
        var dashboardDemographicAggregates = createDemographicsAggregators as DashboardDemographicAggregate[] ??
                                             createDemographicsAggregators.ToArray();
        foreach (var student in studentsQuery)
        {
            foreach (var item in dashboardAnalyticAggregates) UpdateAggregate(item, student, totalStudents);

            foreach (var item in dashboardDemographicAggregates)
            {
                if (item.Key!.Contains($"R{student.RaceCode1!}") || DashboardUtils.ParseGender(item, student))
                    item.DemographicAggregate++;

                if (item.Key!.Equals("T1")) item.DemographicAggregate++;
            }
        }

        var result = new D81Page
        {
            Analytics = dashboardAnalyticAggregates,
            Demographics = dashboardDemographicAggregates
        };
        return result;
    }

    private static short Level(string filter)
    {
        var a = filter.IndexOf("A9e41", StringComparison.Ordinal) + 5;
        var pattern = @"^\d+";
        var rg = new Regex(pattern);
        var level = Convert.ToInt16(rg.Match(filter[a..]).Value);
        //IQueryable<Student> studentsQuery = from student in context.Students where student.Org!.OrgId && filterStudent(student, filter) == org select student;
        var selectXpr = GetSelectXpr("A9e41", level);
        return level;
    }
}