using lb_frontend_02.Server.Controllers.API_v1.StudentPage;

namespace lb_frontend_02.Server.Controllers.API_v1.DashboardPage;

public class D81Page
{
    public IEnumerable<DashboardDemographicAggregate>? Demographics { get; set; }
    public IEnumerable<DashboardAnalyticAggregate>? Analytics { get; set; }

    public IEnumerable<DashboardStudentDetailed>? Students { get; set; }
}

public class D81Table
{
    public IEnumerable<DashboardStudentDetailed>? Students { get; set; }
}

public class DashboardAnalyticAggregate
{
    public required string Key { get; init; }
    public string? AnalyticTitle { get; set; }
    public float? AnalyticLevelAmount { get; set; }
    public string? AnalyticLevelText { get; set; }
    public string? AnalyticDescription { get; set; }
    public IEnumerable<DashboardAnalyticCategory>? AnalyticCategories { get; set; }

    private static string ParseAnalyticsImage(string id)
    {
        if (id == "T1") return "Students Enrolled";

        return "";
    }
}

public class DashboardAnalyticCategory
{
    public required string Key { get; set; }
    public int? AnalyticCategoryStudentAmount { get; set; }
}

public class DashboardDemographicAggregate
{
    public required string Key { get; init; }
    public string? DemographicTitle => ParseDemographicTitle(Key);
    public int? DemographicAggregate { get; set; }

    private static string ParseDemographicTitle(string id)
    {
        if (id == "T1") return "Students Enrolled";
        if (id == "R100") return "American Indian or Alaska Native";
        if (id == "R201") return "Chinese";
        if (id == "R202") return "Japanese";
        if (id == "R203") return "Korean";
        if (id == "R204") return "Vietnamese";
        if (id == "R205") return "Asian Indian";
        if (id == "R206") return "Laotian";
        if (id == "R207") return "Cambodian";
        if (id == "R208") return "Hmong";
        if (id == "R299") return "Other Asian";
        if (id == "R301") return "Hawaiian";
        if (id == "R302") return "Guamanian";
        if (id == "R303") return "Samoan";
        if (id == "R304") return "Tahitian";
        if (id == "R399") return "Other Pacific Islander";
        if (id == "R400") return "Filipino";
        if (id == "R600") return "Black or African American";
        if (id == "R700") return "White";
        if (id == "G1") return "Male";
        if (id == "G2") return "Female";
        if (id == "G3") return "Other/Unknown";

        return "";
    }
}

public class DashboardStudentDetailed : Student
{
    public required string Key { get; init; }
}