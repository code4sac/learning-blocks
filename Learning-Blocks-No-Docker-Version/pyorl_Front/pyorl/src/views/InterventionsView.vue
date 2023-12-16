<script lang="ts" setup>
import AppStatistic from "@/components/app/AppStatistic.vue";
import StyleDemoTable from "@/components/StyleDemoTable";
import AppNavSide from "@/components/app/AppNavSide.vue";
// import DemographicPieChart from "@/components/DemographicBarChart";
import { ref } from 'vue';
import jsonData from '../../demo.json';

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
)

const dataList = [
        {jsonData: studentsByGender, containerId: "GenderPieChart"},
        {jsonData: studentsByGrade, containerId: "GradePieChart"},
        {jsonData: studentsByGrade, containerId: "GradePieChart1"}
      ]
const showDemographicGraphs = ref(false);

const onClickShowDemographicGraphs = () => {

}
</script>

<template>
  <el-container direction="vertical">
    <div class="statistic-container">
      <AppStatistic/>
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
  max-width: 1700px;
}

.dashboard-table {
  width: auto;
}
</style>
