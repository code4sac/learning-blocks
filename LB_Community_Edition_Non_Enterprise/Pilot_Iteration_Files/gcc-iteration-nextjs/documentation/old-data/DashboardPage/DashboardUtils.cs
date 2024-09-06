using lb_frontend_02.Server.Controllers.API_v1.StudentPage;

namespace lb_frontend_02.Server.Controllers.API_v1.DashboardPage;

public static class DashboardUtils
{
    private static IEnumerable<DashboardAnalyticCategory> GenerateCategories()
    {
        return new List<DashboardAnalyticCategory>
        {
            new()
            {
                Key = "Very Low",
                AnalyticCategoryStudentAmount = 0
            },
            new()
            {
                Key = "Low",
                AnalyticCategoryStudentAmount = 0
            },
            new()
            {
                Key = "Medium",
                AnalyticCategoryStudentAmount = 0
            },
            new()
            {
                Key = "High",
                AnalyticCategoryStudentAmount = 0
            },
            new()
            {
                Key = "Very High",
                AnalyticCategoryStudentAmount = 0
            }
        };
    }

    public static IEnumerable<DashboardDemographicAggregate> CreateDemographicsAggregators()
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

    public static IEnumerable<DashboardAnalyticAggregate> CreateAnalyticAggregators()
    {
        return new List<DashboardAnalyticAggregate>
        {
            new()
            {
                Key = "A9e41", AnalyticTitle = "Chronic Absenteeism",
                AnalyticDescription = "Who is chronically absent (less than 10% attendance).",
                AnalyticLevelAmount = 0,
                AnalyticCategories = GenerateCategories()
            },
            new()
            {
                Key = "Aaa59", AnalyticTitle = "Suspension Rate", AnalyticDescription = "Cohort data.",
                AnalyticLevelAmount = 0,
                AnalyticCategories = GenerateCategories()
            },
            new()
            {
                Key = "A4793", AnalyticTitle = "Graduation Rate", AnalyticDescription = "Graduation rate.",
                AnalyticLevelAmount = 0,
                AnalyticCategories = GenerateCategories()
            },
            new()
            {
                Key = "A7924", AnalyticTitle = "LTEL",
                AnalyticDescription =
                    "LTEL List (students who arent on track to keeping up with their english as a secondary language).",
                AnalyticLevelAmount = 0,
                AnalyticCategories = GenerateCategories()
            },
            new()
            {
                Key = "A2fcb", AnalyticTitle = "College and Career",
                AnalyticDescription = "College and career indicators.",
                AnalyticLevelAmount = 0,
                AnalyticCategories = GenerateCategories()
            },
            new()
            {
                Key = "Ae5f9", AnalyticTitle = "Unduplicated Count", AnalyticDescription = "Unduplicated Count.",
                AnalyticLevelAmount = 0,
                AnalyticCategories = GenerateCategories()
            },
            new()
            {
                Key = "A418f", AnalyticTitle = "English Language Arts", AnalyticDescription = "English score.",
                AnalyticLevelAmount = 0,
                AnalyticCategories = GenerateCategories()
            },
            new()
            {
                Key = "A0d7f", AnalyticTitle = "Mathematics", AnalyticDescription = "Math score.",
                AnalyticLevelAmount = 0,
                AnalyticCategories = GenerateCategories()
            }
        };
    }

    public static bool ParseGender(DashboardDemographicAggregate item, Student student)
    {
        if (item.Key! == "G1" && student.Gender == "M") return true;
        if (item.Key! == "G2" && student.Gender == "F") return true;
        if (item.Key! == "G3" && student.Gender != "F" && student.Gender != "M") return true;
        return false;
    }

    // public static int? CalculateAnalyticLevel(string itemKey, Student student, int totalStudents)
    // {
    //     switch (itemKey)
    //     {
    //         case "A100":
    //             return student.ChronicAbsenteeism / 
    //         default:
    //     }
    // }
}