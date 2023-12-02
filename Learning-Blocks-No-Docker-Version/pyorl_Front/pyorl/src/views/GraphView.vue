<template>
    <div class="graphContainer">
        <DemographicPieChart
            v-for="(data, index) in dataList"
            :key="index"
            :jsonData="data.jsonData"
            :containerId="data.containerId"
        />
    </div>
</template>
  
<script>
import DemographicPieChart from '../components/DemographicPieChart.vue'
import jsonData from '../../demo.json';
import {ref} from 'vue';

// These two variables are to emulate fetching data from the backend
    const studentsByGender = ref(
        Object.values(jsonData.reduce((accumulator, student) => {
            const name = student.Gender;

            if (accumulator[name]) {
                accumulator[name].value++;
            } else {
                accumulator[name] = { name: String(name), value: 1 };
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
                accumulator[name] = { name: String(name), value: 1 };
            }

            return accumulator;
        }, {}))
    );

    export default {
        name: 'GraphView',
        components: {
            DemographicPieChart
        },
        data(){
            return {
                dataList:[
                    {jsonData:studentsByGender, containerId:"GenderPieChart"}, 
                    {jsonData:studentsByGrade, containerId:"GradePieChart"}, 
                    {jsonData:studentsByGrade, containerId:"GradePieChart1"}, 
                    {jsonData:studentsByGrade, containerId:"GradePieChart2"}
                ]
            };
        }
    }
</script>
  
<style>
  .graphContainer{
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
    align-items: center;
  }
</style>
  