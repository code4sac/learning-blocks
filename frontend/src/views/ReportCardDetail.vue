<template>
  <h4>School ID: {{ schoolId }}</h4>
  <h4>Student ID: {{ studentId }}</h4>
  <h4>API Key: {{ apiKey }}</h4>
  <h4>Result</h4>
  <!-- Add bottom here  -->
  <v-btn @click="downLoadData">
    Download
  </v-btn>
  <aries-data-table :data-column-headers="reportCardColumnHeaders" :data-rows="reportCardRows"></aries-data-table>
  
</template>

<script>
import AriesDataTable from '@/components/AriesDataTable.vue'
import {filterTableData} from "@/composables/filterTableData.js"
import {createCSVDownload,transformData } from '@/lib/CsvParser.js'
import {onMounted} from "vue"


export default {
  name: 'ReportDetail',
  components: {AriesDataTable},
  data: () => ({
    apiKey: '',
    tableData: {
      type: Array,
      default: () => {
        return [{
          'StudentID': 0,
          'StudentReportCardCourses': [{
            'SchoolCode': 0,
            'CourseID': '',
            'CourseTitle': '',
            'Period': '',
            'SectionNumber': 0,
            'TeacherNumber': 0,
            'MarkingPeriodGrades': [{
              'PrimaryStaffID': 0,
              'Hours': 0.0,
              'AttendanceBasedGradesIndicator': '',
              'MarkingPeriod': 0,
              'Mark': '',
              'Credit': 0.0,
              'Comment1Code': '',
              'Comment2Code': '',
              'Comment3Code': '',
              'CitizenshipCode': '',
              'WorkHabitsCode': '',
              'TotalAbsences': 0,
              'TotalTardies': 0,
              'TotalDaysEnrolled': 0,
              'TotalDaysPresent': 0,
              'TotalExcusedAbsences': 0,
              'TotalUnExcusedAbsences': 0,
              'TotalDaysOfSuspension': 0,
            }]
          }]
        }]
      }
    }
  }),
  setup() {
    onMounted(() => {
      const {ftd} = filterTableData()
      
      return ftd
    })
  },
  methods:{
    downLoadData(){
      createCSVDownload(this.tableData,'','ReportCard')     
    }
  },
  computed: {
 
    
    // populates the headers 
    reportCardColumnHeaders() {
      const isObject = (object) => object != null && object.constructor.name === "Object"
      function getKeys(object,keepObjectKeys,skipArrays,keys = [],scope = []) {
        Object.keys(object).forEach(key =>{
            if(keys.length === 7){
              return
            }
            else if(isObject(object[key]) || Array.isArray(object[key]) ){
              getKeys(object[key],keepObjectKeys,skipArrays,keys,scope.concat(object[key]))
            }
            else{
              keys.push(key)
            }
        })
        return keys
      }
      return getKeys(this.tableData)
    },
    // populates the rows
    reportCardRows() {
      function getValues(object,values = [] ,rows = []) {
        
        const headersLength = 7
        const data = transformData(object)
        const StudentID = Object.values(data[0]).join(',')
        
        for(let i = 0; i < data.length; i++){

          values.push(Object.values(data[i]).join(','))
          if(values.length % headersLength == 0 && i > 0 ){

            rows.splice(rows.length,0,[...values])
            values.splice(0,values.length)

            if(i != data.length - 1 && Object.keys(data[i+1]).join(',') != Object.keys(data[0]).join(',')){
              values.splice(0,0,StudentID)
            }
          }
          
        }
        return rows
      }

      let rows = getValues(this.tableData)
      return rows
    },
    schoolId() {
      // return this.tableData[0].schoolId
      return 'Todo'
    },
    studentId() {
    
      return this.tableData[0].studentId
    }
  },
  watch: {
    reportCardData: {
      immediate: true,
      deep: true,
      handler() {
      }
    }
  },
  created() {

    this.tableData = JSON.parse(localStorage.getItem(this.$route.params.localStorageKey))
   
    
    // function breakItDown(data) {
    //   data.reduce((accumulator, currentValue) => {
    //     let values = []
    //     if (typeof currentValue === 'object') {
    //       Object.entries(currentValue).map(value => {
    //         if (typeof value[1] === 'string' | 'number') {
    //           return value[0]
    //         } else {
    //           return 'a'
    //         }
    //       })
    //     }
    //     return values
    //   }, [])
    // }

    // breakItDown(this.tableData)
  },
  mounted() {
   
    // fetch(`http://127.0.0.1:3000/LearningBlocksAPI/demoAriesReportCard?api_type=demo&school_id=994&student_id=99400002&api_key=477abe9e7d27439681d62f4e0de1f5e1`).then((response)=>{
    //       console.log(response)
    //       return response.text()
    //     }
    // ).then((data)=>{
    //       console.log(data)
    //       localStorage.setItem("ariesApiReportCardData", '[{"StudentID":99400002,"StudentReportCardCourses":[{"SchoolCode":994,"CourseID":"0416","CourseTitle":"Spanish I","Period":"1","SectionNumber":1156,"TeacherNumber":730,"MarkingPeriodGrades":[{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":1,"Mark":"A","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":29,"TotalDaysPresent":29,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":2,"Mark":"A-","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"N","WorkHabitsCode":"O","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":28,"TotalDaysPresent":28,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":3,"Mark":"A-","Credit":5.0,"Comment1Code":"E","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":88,"TotalDaysPresent":88,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":4,"Mark":"A-","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":2,"TotalTardies":0,"TotalDaysEnrolled":92,"TotalDaysPresent":90,"TotalExcusedAbsences":1,"TotalUnExcusedAbsences":1,"TotalDaysOfSuspension":0}]},{"SchoolCode":994,"CourseID":"0968","CourseTitle":"Leadership","Period":"2","SectionNumber":2008,"TeacherNumber":721,"MarkingPeriodGrades":[{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":1,"Mark":"A","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":29,"TotalDaysPresent":29,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":2,"Mark":"A","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":28,"TotalDaysPresent":28,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":3,"Mark":"A","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"S","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":88,"TotalDaysPresent":88,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":4,"Mark":"C","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":2,"TotalTardies":0,"TotalDaysEnrolled":92,"TotalDaysPresent":90,"TotalExcusedAbsences":2,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0}]},{"SchoolCode":994,"CourseID":"0674","CourseTitle":"Phys Science,CP","Period":"3","SectionNumber":3134,"TeacherNumber":807,"MarkingPeriodGrades":[{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":1,"Mark":"A-","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":29,"TotalDaysPresent":29,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":2,"Mark":"A-","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"S","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":28,"TotalDaysPresent":28,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":3,"Mark":"A-","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"S","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":88,"TotalDaysPresent":88,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":4,"Mark":"A-","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"S","WorkHabitsCode":"","TotalAbsences":1,"TotalTardies":0,"TotalDaysEnrolled":92,"TotalDaysPresent":91,"TotalExcusedAbsences":1,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0}]},{"SchoolCode":994,"CourseID":"0645","CourseTitle":"Adv Algebra CP","Period":"4","SectionNumber":4009,"TeacherNumber":725,"MarkingPeriodGrades":[{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":1,"Mark":"B","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":29,"TotalDaysPresent":29,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":2,"Mark":"B","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"S","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":28,"TotalDaysPresent":28,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":3,"Mark":"B","Credit":5.0,"Comment1Code":"","Comment2Code":"E","Comment3Code":"","CitizenshipCode":"S","WorkHabitsCode":"","TotalAbsences":1,"TotalTardies":0,"TotalDaysEnrolled":88,"TotalDaysPresent":87,"TotalExcusedAbsences":1,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":4,"Mark":"C","Credit":5.0,"Comment1Code":"E","Comment2Code":"","Comment3Code":"","CitizenshipCode":"S","WorkHabitsCode":"","TotalAbsences":1,"TotalTardies":0,"TotalDaysEnrolled":92,"TotalDaysPresent":91,"TotalExcusedAbsences":1,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0}]},{"SchoolCode":994,"CourseID":"0010","CourseTitle":"PE 9","Period":"5","SectionNumber":5065,"TeacherNumber":607,"MarkingPeriodGrades":[{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":1,"Mark":"A","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":1,"TotalTardies":0,"TotalDaysEnrolled":29,"TotalDaysPresent":28,"TotalExcusedAbsences":1,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":2,"Mark":"A","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"S","WorkHabitsCode":"","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":28,"TotalDaysPresent":28,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":3,"Mark":"A","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":2,"TotalTardies":0,"TotalDaysEnrolled":88,"TotalDaysPresent":86,"TotalExcusedAbsences":2,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":4,"Mark":"A","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":2,"TotalTardies":0,"TotalDaysEnrolled":92,"TotalDaysPresent":90,"TotalExcusedAbsences":2,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0}]},{"SchoolCode":994,"CourseID":"0301","CourseTitle":"English 9 Cp","Period":"6","SectionNumber":6089,"TeacherNumber":694,"MarkingPeriodGrades":[{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":1,"Mark":"A","Credit":5.0,"Comment1Code":"E","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":1,"TotalTardies":0,"TotalDaysEnrolled":29,"TotalDaysPresent":28,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":1,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":2,"Mark":"A+","Credit":5.0,"Comment1Code":"E","Comment2Code":"","Comment3Code":"","CitizenshipCode":"S","WorkHabitsCode":"S","TotalAbsences":0,"TotalTardies":0,"TotalDaysEnrolled":28,"TotalDaysPresent":28,"TotalExcusedAbsences":0,"TotalUnExcusedAbsences":0,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":3,"Mark":"A","Credit":5.0,"Comment1Code":"E","Comment2Code":"","Comment3Code":"","CitizenshipCode":"","WorkHabitsCode":"","TotalAbsences":2,"TotalTardies":0,"TotalDaysEnrolled":88,"TotalDaysPresent":86,"TotalExcusedAbsences":1,"TotalUnExcusedAbsences":1,"TotalDaysOfSuspension":0},{"PrimaryStaffID":0,"Hours":0.0,"AttendanceBasedGradesIndicator":"","MarkingPeriod":4,"Mark":"A","Credit":5.0,"Comment1Code":"","Comment2Code":"","Comment3Code":"","CitizenshipCode":"S","WorkHabitsCode":"","TotalAbsences":3,"TotalTardies":0,"TotalDaysEnrolled":92,"TotalDaysPresent":89,"TotalExcusedAbsences":2,"TotalUnExcusedAbsences":1,"TotalDaysOfSuspension":1}]}]}]')
    //     }
    // ).catch((error)=>{
    //       console.log(error)
    //     }
    // )
  }
}
</script>

<style scoped>

</style>