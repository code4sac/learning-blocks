import {DemographicData} from "./DemographicData";

export default async function getStudentData():  Promise<Array<DemographicData>>{
  const { default: mockData } = await import("./studentMockData01.json", { assert: { type: "json" } });
  return mockData.map(it => {
    return new DemographicData(
      it["Student ID"],
      new Date(it.Birthdate),
      it.Gender,
      it.Grade,
      it.Race1,
      it["Birth Country"],
      it["Birth State"],
      it["Birth City"],
      it["DST of Residence"]
    );
  })
}
