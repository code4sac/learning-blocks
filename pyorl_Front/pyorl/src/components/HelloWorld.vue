<template>
  <div class="hello">
    <template v-if="studentRecord">
      <h3>Found:</h3>
      <p>Student ID: {{ studentRecord.StudentID }}</p>
      <p>Academic Year: {{ studentRecord.AcademicYear }}</p>
      <p>Grade: {{ studentRecord.Grade }}</p>
      <h3>Download Student Information:</h3>
       <p>
       <a href="http://127.0.0.1:8000/download-data" target="_blank"> Download Json</a> ||
       <a href="http://127.0.0.1:8000/download-csv" target="_blank"> Download CSV</a>
       </p>
    </template>






  </div>
</template>

<script lang="ts">
import axios from 'axios';
import { Options, Vue } from 'vue-class-component';

@Options({
  props: {
    msg: String
  }
})
export default class HelloWorld extends Vue {
  msg!: string;
  studentRecord: any = null;

  mounted() {
    this.fetchStudentRecords();
  }

  fetchStudentRecords() {
    const URL = 'http://127.0.0.1:8000/student-data';
    axios.get(URL)
      .then(response => {
        this.studentRecord = response.data[0];
      })
      .catch(error => {
        console.error('Error fetching student records:', error);
      });
  }
}
</script>
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
