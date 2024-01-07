export class DemographicData {
  studentId: number
  birthdate: Date
  gender: String
  grade: number
  race1: number | String
  birthCountry: String
  birthState: String
  birthCity: String
  DSTOfResidence: number | String

  constructor(studentId: number,
              birthdate: Date,
              gender: String,
              grade: number,
              race1: number | String,
              birthCountry: String,
              birthState: String,
              birthCity: String,
              DSTOfResidence: number | String) {
    this.studentId = studentId;
    this.birthdate = birthdate;
    this.gender = gender;
    this.grade = grade;
    this.race1 = race1;
    this.birthCountry = birthCountry;
    this.birthState = birthState;
    this.birthCity = birthCity;
    this.DSTOfResidence = DSTOfResidence;
  }
}