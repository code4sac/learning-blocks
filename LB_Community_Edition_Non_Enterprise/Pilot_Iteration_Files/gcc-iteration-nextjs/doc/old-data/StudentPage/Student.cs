using lb_frontend_02.Server.Controllers.API_v1.Utilities;

namespace lb_frontend_02.Server.Controllers.API_v1.StudentPage;

public enum Gender
{
    M,
    F
}

public enum EthnicityCode
{
    N,
    Y
}

public class Student
{
    public int? StudentId { get; set; }
    public int? SchoolCode { get; set; }
    public int? Absenteeism { get; set; }
    public string? LastName { get; set; }
    public string? FirstName { get; set; }
    public string? MiddleName { get; set; }
    public int? FailingGrades { get; set; }
    public int? LowGpa { get; set; }
    public int? HsReadiness { get; set; }
    public string? Gender { get; set; }
    public int? Grade { get; set; }
    public int? Ltel { get; set; }
    public int? UnduplicatedCount { get; set; }
    public int? ChronicAbsenteeism { get; set; }
    public int? SuspensionRate { get; set; }
    public string? EthnicityCode { get; set; }
    public string? RaceCode1 { get; set; }
    public int? CohortData { get; set; }
    public int? GraduationRate { get; set; }
    public int? CollegeAndCareer { get; set; }
    public string? HomeLanguageCode { get; set; }
    public string? LanguageFluencyCode { get; set; }
    public string? CorrespondenceLanguageCode { get; set; }
    public int? ELA { get; set; }
    public int? MATH { get; set; }


    public Org? Org { get; set; }
}