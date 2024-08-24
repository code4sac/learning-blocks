using System.Text.Json;
using lb_frontend_02.Server.Controllers.API_v1.StudentPage;

namespace lb_frontend_02.Server.Controllers.API_v1.Utilities;

public static class DatabaseUtilities
{
    public static Org CreateDemoOrg()
    {
        return new Org
        {
            OrgId = 994
        };
    }

    public static Student GenerateRandomAnalytics(Student student)
    {
        throw new NotImplementedException();
    }

    public static class JsonFileReader
    {
        public static T Read<T>(string filePath)
        {
            var text = File.ReadAllText(filePath);
            return JsonSerializer.Deserialize<T>(text)!;
        }
    }
}