<template>
  <v-container>
    <!--    <h1 class="header center orange-text">Aries Report Cards</h1>-->
    <!--    <h5 class="header col s12 light">Find student data and download reports within the Aries school system</h5>-->
    <!--    <v-btn>Learn more</v-btn>-->
  </v-container>
  <v-form>
    <v-container>
      <v-row>
        <v-col cols="4">
          <v-select v-model="selectedQuery" :items="queryTypes" label="Query type"></v-select>
        </v-col>
      </v-row>
      <v-row>
        <v-col v-for="field in queryFields" :key="field.model" cols="12" md="4" >
          <v-text-field
              v-model="field.model"
              :label="field.label"
              :required="field.required ? field.required : false"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-switch v-model="productionApi" label="Production API"></v-switch>
      <br>
      <v-btn color="blue" type="submit" @click.stop.prevent="submit">Generate query</v-btn>
    </v-container>
  </v-form>
</template>

<script>
export default {
  data: () => ({
    queryTypes: [
      'Report card',
      'Students',
      'Enrollment'
    ],
    returnQuery:[],
    selectedQuery: '',
    productionApi: false,
    schoolId: '994',
    studentId: '99400002',
    apiKey: '477abe9e7d27439681d62f4e0de1f5e1',
  }),
  computed: {
    queryFields() {
      let fields = []
      switch (this.selectedQuery) {
        case 'Report card':
          fields.push({
            'model': 'schoolId',
            'label': 'School ID',
            'required': true
          }, {
            'model': 'studentId',
            'label': 'Student ID',
            'required': true
          }, {
            'model': 'apiKey',
            'label': 'API Key',
            'required': true
          })
          break
        case 'Students':
          fields.push({
            'model': 'schoolId',
            'label': 'School ID',
            'required': true
          }, {
            'model': 'apiKey',
            'label': 'API Key',
            'required': true
          })
          break
        case 'Enrollment':
          fields.push({
            'label': 'SchoolID',
            'model': 'schoolId',
            'required': true
            },
            {
              'label': 'StudentID',
              'model': 'studentId',
              'required': true
            },
            {
              'label': 'LastName',
              'model': 'lastname',
              'required': true
            },
            {
            'label': 'APIKey',
            'model': 'apiKey',
            'required': true
          })
          break
      }
      console.log('fields',fields)
      
      return fields

    }
  },
  methods: {
    submit() {
      if (this.selectedQuery === 'Report card') {
        // fetch the json data
        const uniqueIdentifier = 'schools994_reportcard99400002_shorty'
        fetch(`${uniqueIdentifier}.json`).then(response => {
          response.text().then(response => {
            localStorage.setItem(uniqueIdentifier, response)
            this.$router.push({
              name: 'report',
              params: {localStorageKey: uniqueIdentifier}
            }).catch(error => console.log(error))
          }).catch(error => console.log(error))
        }).catch(error => console.log(error))

      } else if (this.selectedQuery === 'Students') {
        const uniqueIdentifier = 'schools994_students_grade11'
        fetch(`${uniqueIdentifier}.json`).then(response => {
          response.text().then(response => {
            localStorage.setItem(uniqueIdentifier, response)
            this.$router.push({
              name: `students`,
              params: {localStorageKey: uniqueIdentifier}
            }).catch(error => console.log(error))
          }).catch(error => console.log(error))
        }).catch(error => console.log(error))
      }
        else if (this.selectedQuery === 'Enrollment') {
        const uniqueIdentifier = 'enrollment'
        fetch(`${uniqueIdentifier}.json`).then(response => {
          response.text().then(response => {
            localStorage.setItem(uniqueIdentifier, response)
            this.$router.push({
              name: `enrollment`,
              params: {localStorageKey: uniqueIdentifier}
            }).catch(error => console.log(error))
          }).catch(error => console.log(error))
        }).catch(error => console.log(error))
      }

    },
    getQueryField(){
      this.returnQuery = this.queryFields()
      console.log('here',this.returnQuery)
    }
  },
  created() {
    this.selectedQuery = this.queryTypes[0]
    
  },
  mounted() {
    // fetch(`http://127.0.0.1:3000/LearningBlocksAPI/demoAriesReportCard?api_type=demo&school_id=994&student_id=99400002&api_key=477abe9e7d27439681d62f4e0de1f5e1`).then((response)=>{
    //       console.log(response)
    //       return response.text()
    //     }
    // ).then((data)=>{
    //       console.log(data)
    //       localStorage.setItem('ariesApiReportCardData', '[{"StudentID":99400002,"StudentReportCardCourses":[{"SchoolCode":994,"CourseID":"0416","CourseTitle":"Spanish I","Period":"1","SectionNumber":1156,"TeacherNumber":730,"MarkingPeriodGrades":[{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":1,"Mark":"A","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":29,"TotalDaysPresent":29,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":2,"Mark":"A-","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"N","WorkHabitsCode":"O","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":28,"TotalDaysPresent":28,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":3,"Mark":"A-","Credit":5.0,"Comment1Code":"E","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":88,"TotalDaysPresent":88,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":4,"Mark":"A-","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":2,"TotalTardies":0,"TotalDaysEnrolled":92,"TotalDaysPresent":90,"TotalExcusedAbsences":1,"TotalUnExcusedAbsences":1,"TotalDaysOfSuspension":0}]},{"SchoolCode":994,"CourseID":"0968","CourseTitle":"Leadership","Period":"2","SectionNumber":2008,"TeacherNumber":721,"MarkingPeriodGrades":[{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":1,"Mark":"A","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":29,"TotalDaysPresent":29,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":2,"Mark":"A","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":28,"TotalDaysPresent":28,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":3,"Mark":"A","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"S","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":88,"TotalDaysPresent":88,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":4,"Mark":"C","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":2,"TotalTardies":0,"TotalDaysEnrolled":92,"TotalDaysPresent":90,"TotalExcusedAbsences":2,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0}]},{"SchoolCode":994,"CourseID":"0674","CourseTitle":"Phys Science,CP","Period":"3","SectionNumber":3134,"TeacherNumber":807,"MarkingPeriodGrades":[{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":1,"Mark":"A-","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":29,"TotalDaysPresent":29,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":2,"Mark":"A-","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"S","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":28,"TotalDaysPresent":28,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":3,"Mark":"A-","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"S","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":88,"TotalDaysPresent":88,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":4,"Mark":"A-","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"S","WorkHabitsCode":"","TotalAbsences":1,"TotalTardies":0,"TotalDaysEnrolled":92,"TotalDaysPresent":91,"TotalExcusedAbsences":1,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0}]},{"SchoolCode":994,"CourseID":"0645","CourseTitle":"Adv Algebra CP","Period":"4","SectionNumber":4009,"TeacherNumber":725,"MarkingPeriodGrades":[{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":1,"Mark":"B","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":29,"TotalDaysPresent":29,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":2,"Mark":"B","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"S","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":28,"TotalDaysPresent":28,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":3,"Mark":"B","Credit":5.0,"Comment1Code":"","Comment2Code":"E","Comment3Code":"","CitizenshipCode":"S","WorkHabitsCode":"","TotalAbsences":1,"TotalTardies":0,"TotalDaysEnrolled":88,"TotalDaysPresent":87,"TotalExcusedAbsences":1,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":4,"Mark":"C","Credit":5.0,"Comment1Code":"E","Comment2Code":"","Comment3Code":"","CitizenshipCode":"S","WorkHabitsCode":"","TotalAbsences":1,"TotalTardies":0,"TotalDaysEnrolled":92,"TotalDaysPresent":91,"TotalExcusedAbsences":1,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0}]},{"SchoolCode":994,"CourseID":"0010","CourseTitle":"PE 9","Period":"5","SectionNumber":5065,"TeacherNumber":607,"MarkingPeriodGrades":[{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":1,"Mark":"A","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":1,"TotalTardies":0,"TotalDaysEnrolled":29,"TotalDaysPresent":28,"TotalExcusedAbsences":1,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":2,"Mark":"A","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"S","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":28,"TotalDaysPresent":28,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":3,"Mark":"A","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":2,"TotalTardies":0,"TotalDaysEnrolled":88,"TotalDaysPresent":86,"TotalExcusedAbsences":2,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":4,"Mark":"A","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":2,"TotalTardies":0,"TotalDaysEnrolled":92,"TotalDaysPresent":90,"TotalExcusedAbsences":2,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0}]},{"SchoolCode":994,"CourseID":"0301","CourseTitle":"English 9 Cp","Period":"6","SectionNumber":6089,"TeacherNumber":694,"MarkingPeriodGrades":[{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":1,"Mark":"A","Credit":5.0,"Comment1Code":"E","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":1,"TotalTardies":0,"TotalDaysEnrolled":29,"TotalDaysPresent":28,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":1,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":2,"Mark":"A+","Credit":5.0,"Comment1Code":"E","Comment2Code":"","Comment3Code":"","CitizenshipCode":"S","WorkHabitsCode":"S","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":28,"TotalDaysPresent":28,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":3,"Mark":"A","Credit":5.0,"Comment1Code":"E","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":2,"TotalTardies":0,"TotalDaysEnrolled":88,"TotalDaysPresent":86,"TotalExcusedAbsences":1,"TotalUnExcusedAbsences":1,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":4,"Mark":"A","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"S","WorkHabitsCode":"","TotalAbsences":3,"TotalTardies":0,"TotalDaysEnrolled":92,"TotalDaysPresent":89,"TotalExcusedAbsences":2,"TotalUnExcusedAbsences":1,"TotalDaysOfSuspension":1}]}]}]')
    //     }
    // ).catch((error)=>{
    //       console.log(error)
    //     }
    // )
  }
}
</script>