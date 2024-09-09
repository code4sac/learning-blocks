using lb_frontend_02.Server.Controllers.API_v1.StudentPage;
using lb_frontend_02.Server.Controllers.API_v1.Utilities;

namespace lb_frontend_02.Server.Data;

public static class DbInitializer
{
    public static void Initialize(ApplicationDbContext context)
    {
        context.Database.EnsureCreated();
        if (context.Students.Any()) return;

        var org = DatabaseUtilities.CreateDemoOrg();

        var students = DatabaseUtilities.JsonFileReader.Read<Student[]>(@"Data\2024-03-11T190828.200.json");
        foreach (var student in students)
        {
            student.Org = org;
            var random = new Random();
            student.ChronicAbsenteeism = random.Next(0, 100);
            student.SuspensionRate = random.Next(0, 100);
            student.GraduationRate = random.Next(0, 100);
            student.Ltel = random.Next(0, 100);
            student.CollegeAndCareer = random.Next(0, 100);
            student.UnduplicatedCount = random.Next(0, 100);
            student.ELA = random.Next(0, 100);
            student.MATH = random.Next(0, 100);
            context.Students.Add(student);
        }

        context.SaveChanges();
    }
}