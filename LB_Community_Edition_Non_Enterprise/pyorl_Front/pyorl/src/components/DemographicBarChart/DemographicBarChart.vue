<script lang="ts">
import * as d3 from 'd3';
import {Vue} from "vue-class-component";
import {DemographicData} from "./DemographicData";
import getStudentData from "./studentData";

type DemographicBarChartData = {
  gradeLevel: number
  numberOfStudents: number
}
export default class DemographicBarChart extends Vue {
  async mounted() {
    const demographicData: Array<DemographicData> = await getStudentData();
    let totalNumberOfStudentsInGrade: Array<DemographicBarChartData> = demographicData.reduce((accumulator, currentValue) => {
      const dataIndex = accumulator.findIndex(it => it.gradeLevel === currentValue.grade)
      if (dataIndex > -1) {
        (accumulator as any)[dataIndex].numberOfStudents++;
      } else {
        (accumulator as any).push({gradeLevel: currentValue.grade, numberOfStudents: 1});
      }
      return accumulator;
    }, [] as Array<DemographicBarChartData>);

    let margin = {top: 30, right: 30, bottom: 70, left: 60},
      width = 460 - margin.left - margin.right,
      height = 400 - margin.top - margin.bottom;

    let svg = d3.select("#barChart01")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", `translate(${margin.left},${margin.top})`);

    let x = d3.scaleBand()
      .range([0, width])
      .domain(totalNumberOfStudentsInGrade.map(d => d.gradeLevel.toString()))
      .padding(0.2);
    svg.append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(d3.axisBottom(x))
      .selectAll("text")
      .attr("transform", "translate(-10,0)rotate(-45)")
      .style("text-anchor", "end");

    let y = d3.scaleLinear()
      .domain([0, 10])
      .range([height, 0]);
    svg.append("g")
      .call(d3.axisLeft(y));

    svg.selectAll("barChart01Bars")
      .data(totalNumberOfStudentsInGrade)
      .enter()
      .append("rect")
      .attr("x", (d: DemographicBarChartData) => (x(d.gradeLevel.toString()) as number))
      .attr("y", (d: DemographicBarChartData) => y(d.numberOfStudents))
      .attr("width", x.bandwidth())
      .attr("height", (d: DemographicBarChartData) => height - y(d.numberOfStudents))
      .attr("fill", "#69b3a2")
  }
}
</script>

<template>
  <div>
    <p>Student Demographic Data</p>
    <svg id="barChart01"></svg>
  </div>
</template>

<style scoped>

</style>
