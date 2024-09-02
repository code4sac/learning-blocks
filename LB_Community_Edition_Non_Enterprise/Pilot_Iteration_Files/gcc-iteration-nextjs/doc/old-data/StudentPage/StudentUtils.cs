using lb_frontend_02.Server.Controllers.API_v1.DashboardPage;

namespace lb_frontend_02.Server.Controllers.API_v1.StudentPage;

public class StudentUtils
{
    public static IEnumerable<DashboardDemographicAggregate> CreateDemographics()
    {
        return new List<DashboardDemographicAggregate>
        {
            new() { Key = "R100", DemographicAggregate = 0 },
            new() { Key = "R201", DemographicAggregate = 0 },
            new() { Key = "R202", DemographicAggregate = 0 },
            new() { Key = "R203", DemographicAggregate = 0 },
            new() { Key = "R204", DemographicAggregate = 0 },
            new() { Key = "R205", DemographicAggregate = 0 },
            new() { Key = "R206", DemographicAggregate = 0 },
            new() { Key = "R207", DemographicAggregate = 0 },
            new() { Key = "R208", DemographicAggregate = 0 },
            new() { Key = "R299", DemographicAggregate = 0 },
            new() { Key = "R301", DemographicAggregate = 0 },
            new() { Key = "R302", DemographicAggregate = 0 },
            new() { Key = "R303", DemographicAggregate = 0 },
            new() { Key = "R304", DemographicAggregate = 0 },
            new() { Key = "R399", DemographicAggregate = 0 },
            new() { Key = "R400", DemographicAggregate = 0 },
            new() { Key = "R600", DemographicAggregate = 0 },
            new() { Key = "R700", DemographicAggregate = 0 },
            new() { Key = "G1", DemographicAggregate = 0 },
            new() { Key = "G2", DemographicAggregate = 0 },
            new() { Key = "G3", DemographicAggregate = 0 },
            new() { Key = "T1", DemographicAggregate = 0 }
        };
    }

    public static bool ParseGender(DashboardDemographicAggregate item, Student student)
    {
        if (item.Key! == "G1" && student.Gender == "M") return true;
        if (item.Key! == "G2" && student.Gender == "F") return true;
        if (item.Key! == "G3" && student.Gender != "F" && student.Gender != "M") return true;
        return false;
    }
}