<template>
  <h4>Result</h4>
  <v-btn @click="buttonDownload">
      Download
  </v-btn>
  <aries-data-table :data-column-headers="studentsColumnHeaders" :data-rows="studentsRows">
  </aries-data-table>
</template>

<script>
import AriesDataTable from "@/components/AriesDataTable.vue";
import { createCSVDownload } from "@/lib/CsvParser"

export default {
  name: "StudentsInSchoolByGradeDetail",
  components: {AriesDataTable},
  data: () => ({
    tableData: [{
      "StudentID": 0,
      "OldStudentID": 0,
      "CorrespondenceLanguageCode": "",
      "CounselorNumber": 0,
      "StudentPersonalEmailAddress": "",
      "SchoolCode": 0,
      "StudentNumber": 0,
      "StateStudentID": "",
      "LastName": "",
      "FirstName": "",
      "MiddleName": "",
      "LastNameAlias": "",
      "FirstNameAlias": "",
      "MiddleNameAlias": "",
      "Gender": "",
      "Grade": 0,
      "GradeLevelShortDescription": "",
      "GradeLevelLongDescription": "",
      "Birthdate": "",
      "ParentGuardianName": "",
      "HomePhone": "",
      "StudentMobilePhone": "",
      "MailingAddress": "",
      "MailingAddressCity": "",
      "MailingAddressState": "",
      "MailingAddressZipCode": "",
      "MailingAddressZipExt": "",
      "ResidenceAddress": "",
      "ResidenceAddressCity": "",
      "ResidenceAddressState": "",
      "ResidenceAddressZipCode": "",
      "ResidenceAddressZipExt": "",
      "AddressVerified": false,
      "EthnicityCode": "",
      "RaceCode1": "",
      "RaceCode2": "",
      "RaceCode3": "",
      "RaceCode4": "",
      "RaceCode5": "",
      "UserCode1": "",
      "UserCode2": "",
      "UserCode3": "",
      "UserCode4": "",
      "UserCode5": "",
      "UserCode6": "",
      "UserCode7": "",
      "UserCode8": "",
      "UserCode9": "",
      "UserCode10": "",
      "UserCode11": "",
      "UserCode12": "",
      "UserCode13": "",
      "SchoolEnterDate": "",
      "SchoolLeaveDate": "",
      "DistrictEnterDate": "",
      "Track": "",
      "AttendanceProgramCodePrimary": "",
      "AttendanceProgramCodeAdditional1": "",
      "AttendanceProgramCodeAdditional2": "",
      "LockerNumber": "",
      "LowSchedulingPeriod": 0,
      "HighSchedulingPeriod": 0,
      "InactiveStatusCode": "",
      "FamilyKey": 0,
      "LanguageFluencyCode": "",
      "HomeLanguageCode": "",
      "ParentEdLevelCode": "",
      "ParentEmailAddress": "",
      "StudentEmailAddress": "",
      "NetworkLoginID": "",
      "EarlyWarningPoints": 0.0000,
      "HomeRoomTeacherNumber": "",
      "NotificationPreferenceCode": "",
      "NextSchoolCode": 0,
      "NextGrade": 0,
      "NextGradeLevelShortDescription": "",
      "NextGradeLevelLongDescription": "",
      "RecordsReleaseCode": ""
    }]
  }),
  methods:{
    buttonDownload(){
      createCSVDownload(this.tableData,'','StudentsDetail')            
    }
  },
  computed: {
    
    studentsColumnHeaders() {
      return Object.keys(this.tableData[0])
    },
    studentsRows() {
      return this.tableData.reduce((accumulator, currentValue) => [...accumulator, Object.values(currentValue)], [])
    },
  },
  props: {
    localStorageKey: {
      type: String,
      default: ''
    }
  },
  created() {
    this.tableData = JSON.parse(localStorage.getItem(this.$route.params.localStorageKey))
    console.log(this.tableData)
  }
}
</script>

<style scoped>

</style>