<script lang="ts">
import AppStatistic from "@/components/app/AppStatistic.vue";
import StyleDemoTable from "@/components/StyleDemoTable";
import AppNavSide from "@/components/app/AppNavSide.vue";
import DemographicPieChart from "@/components/DemographicPieChart.vue";
import { ref } from 'vue';
import jsonData from '../../demo.json';
import LearningBlocksToolbar from "@/components/app/AppPageHeader.vue";
import AppFooter from "@/components/app/AppFooter.vue";
import AriesDataTable from "@/components/AriesDataTable/AriesDataTable.vue";
import EnrollmentDetails from "@/components/AriesDataTable/EnrollmentDetail.vue";
import ReportDetail from "@/components/AriesDataTable/ReportCardDetail.vue";

// These two variables are to emulate fetching data from the backend
const studentsByGender = ref(
    Object.values(jsonData.reduce((accumulator, student) => {
      const name = student.Gender;

      if (accumulator[name]) {
        accumulator[name].value++;
      } else {
        accumulator[name] = {name: String(name), value: 1};
      }

      return accumulator;
    }, {}))
);

const studentsByGrade = ref(
    Object.values(jsonData.reduce((accumulator, student) => {
      const name = student.Grade;

      if (accumulator[name]) {
        accumulator[name].value++;
      } else {
        accumulator[name] = {name: String(name), value: 1};
      }

      return accumulator;
    }, {}))
);

export default {
  name: 'DashboardView',
  components: {
    StyleDemoTable,
    AppNavSide,
    AppStatistic,
    ReportDetail,
    EnrollmentDetails,
    AriesDataTable,
    AppFooter,
    LearningBlocksToolbar,
    DemographicPieChart
  },
  data() {
    return {
      dataList: [
        {jsonData: studentsByGender, containerId: "GenderPieChart"},
        {jsonData: studentsByGrade, containerId: "GradePieChart"},
        {jsonData: studentsByGrade, containerId: "GradePieChart1"}
      ]
    };
  }
}
</script>

<template>
  <el-container direction="vertical">
    <div class="statistic-container">
      <AppStatistic></AppStatistic>
      <div class="graphContainer">
        <DemographicPieChart
            v-for="(data, index) in dataList"
            :key="index"
            :containerId="data.containerId"
            :jsonData="data.jsonData"
        />
      </div>
    </div>
    <div class="dashboard-main-section">
      <el-aside class="sidebar">
        <AppNavSide></AppNavSide>
      </el-aside>
      <el-container direction="vertical">
        <StyleDemoTable class="dashboard-table"/>
      </el-container>
    </div>
  </el-container>
</template>

<style scoped>
/*
Home page styles.
 */
.pieContainer {
  width: 400px
}

.graphContainer {
  display: flex;
  justify-content: space-evenly;
  flex-wrap: wrap;
  align-items: center
}
.sidebar {
  max-width: 256px;
}

.dashboard-main-section {
  display: flex;
}

.statistic-container {
  padding: 8px 0;
}

.dashboard-table {
  width: auto;
}
</style>
