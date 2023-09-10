<template>
    <svg id="my_dataviz"></svg>
</template>
  
<script>
import * as d3 from 'd3'
import { Vue } from 'vue-class-component';
// import jsonData from '../../demo.json';

export default class DemographicPieChart extends Vue {
    mounted(){
        const width = 450,
            height = 450;

        const jsonData = [
                            {
                                "Student ID": 99000001,
                                "Birthdate": "05/17/2011",
                                "Gender": "M",
                                "Grade": 6,
                                "Race1": 304,
                                "Birth Country": "US",
                                "Birth State": "CA",
                                "Birth City": "Orange",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 99000002,
                                "Birthdate": "12/23/2017",
                                "Gender": "M",
                                "Grade": 1,
                                "Race1": 201,
                                "Birth Country": "",
                                "Birth State": "",
                                "Birth City": "Simi Valley CA",
                                "DST of Residence": 30665300000000
                            },
                            {
                                "Student ID": 99200002,
                                "Birthdate": "05/17/2012",
                                "Gender": "M",
                                "Grade": 6,
                                "Race1": 400,
                                "Birth Country": "US",
                                "Birth State": "CA",
                                "Birth City": "Orange CA",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 99200001,
                                "Birthdate": "12/23/2016",
                                "Gender": "M",
                                "Grade": 1,
                                "Race1": 301,
                                "Birth Country": "",
                                "Birth State": "",
                                "Birth City": "Simi Valley CA",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 99300001,
                                "Birthdate": "05/17/2012",
                                "Gender": "M",
                                "Grade": 6,
                                "Race1": 400,
                                "Birth Country": "",
                                "Birth State": "",
                                "Birth City": "",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 89400001,
                                "Birthdate": "11/11/2005",
                                "Gender": "M",
                                "Grade": 12,
                                "Race1": 700,
                                "Birth Country": "MX",
                                "Birth State": "SO",
                                "Birth City": "Hermosillo",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 99300002,
                                "Birthdate": "11/05/2009",
                                "Gender": "F",
                                "Grade": 8,
                                "Race1": "",
                                "Birth Country": "",
                                "Birth State": "",
                                "Birth City": "",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 99500001,
                                "Birthdate": "02/05/2006",
                                "Gender": "M",
                                "Grade": 11,
                                "Race1": 700,
                                "Birth Country": "",
                                "Birth State": "",
                                "Birth City": "",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 88400001,
                                "Birthdate": "11/11/2005",
                                "Gender": "M",
                                "Grade": 12,
                                "Race1": 700,
                                "Birth Country": "MX",
                                "Birth State": "SO",
                                "Birth City": "Hermosillo",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 88401949,
                                "Birthdate": "12/05/2005",
                                "Gender": "M",
                                "Grade": 12,
                                "Race1": 700,
                                "Birth Country": "US",
                                "Birth State": "",
                                "Birth City": "",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 89400637,
                                "Birthdate": "11/23/2005",
                                "Gender": "F",
                                "Grade": 12,
                                "Race1": 700,
                                "Birth Country": "KR",
                                "Birth State": "",
                                "Birth City": "",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 89400356,
                                "Birthdate": "02/17/2006",
                                "Gender": "M",
                                "Grade": 12,
                                "Race1": 100,
                                "Birth Country": "US",
                                "Birth State": "CA",
                                "Birth City": "Boyle Heights",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 89400416,
                                "Birthdate": "12/03/2008",
                                "Gender": "M",
                                "Grade": 9,
                                "Race1": 600,
                                "Birth Country": "PK",
                                "Birth State": "",
                                "Birth City": "",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 88401782,
                                "Birthdate": "12/13/2008",
                                "Gender": "M",
                                "Grade": 9,
                                "Race1": "",
                                "Birth Country": "US",
                                "Birth State": "",
                                "Birth City": "",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 99400002,
                                "Birthdate": "04/13/2009",
                                "Gender": "F",
                                "Grade": 9,
                                "Race1": 700,
                                "Birth Country": "US",
                                "Birth State": "",
                                "Birth City": "",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 99300003,
                                "Birthdate": "05/31/2010",
                                "Gender": "F",
                                "Grade": 8,
                                "Race1": 700,
                                "Birth Country": "",
                                "Birth State": "",
                                "Birth City": "",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 99400003,
                                "Birthdate": "07/21/2009",
                                "Gender": "F",
                                "Grade": 9,
                                "Race1": 700,
                                "Birth Country": "US",
                                "Birth State": "",
                                "Birth City": "",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 99400004,
                                "Birthdate": "12/24/2007",
                                "Gender": "M",
                                "Grade": 10,
                                "Race1": 700,
                                "Birth Country": "US",
                                "Birth State": "CA",
                                "Birth City": "Inglewood",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 99400006,
                                "Birthdate": "02/26/2008",
                                "Gender": "F",
                                "Grade": 10,
                                "Race1": 400,
                                "Birth Country": "US",
                                "Birth State": "",
                                "Birth City": "",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 99400007,
                                "Birthdate": "09/02/2006",
                                "Gender": "F",
                                "Grade": 12,
                                "Race1": 400,
                                "Birth Country": "US",
                                "Birth State": "",
                                "Birth City": "",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 99400008,
                                "Birthdate": "11/16/2008",
                                "Gender": "F",
                                "Grade": 9,
                                "Race1": 400,
                                "Birth Country": "US",
                                "Birth State": "",
                                "Birth City": "",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 99400009,
                                "Birthdate": "06/23/2006",
                                "Gender": "F",
                                "Grade": 12,
                                "Race1": 700,
                                "Birth Country": "US",
                                "Birth State": "CA",
                                "Birth City": "Monterey Park",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 99300004,
                                "Birthdate": "08/16/2012",
                                "Gender": "F",
                                "Grade": 6,
                                "Race1": "",
                                "Birth Country": "",
                                "Birth State": "",
                                "Birth City": "",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 99400012,
                                "Birthdate": "12/01/2009",
                                "Gender": "F",
                                "Grade": 9,
                                "Race1": "",
                                "Birth Country": "US",
                                "Birth State": "",
                                "Birth City": "",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 99300005,
                                "Birthdate": "04/14/2012",
                                "Gender": "M",
                                "Grade": 6,
                                "Race1": "",
                                "Birth Country": "",
                                "Birth State": "",
                                "Birth City": "",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 88402768,
                                "Birthdate": "07/15/2006",
                                "Gender": "F",
                                "Grade": 12,
                                "Race1": 600,
                                "Birth Country": "JP",
                                "Birth State": "",
                                "Birth City": "",
                                "DST of Residence": ""
                            },
                            {
                                "Student ID": 99100001,
                                "Birthdate": "07/01/2013",
                                "Gender": "M",
                                "Grade": 5,
                                "Race1": 400,
                                "Birth Country": "",
                                "Birth State": "",
                                "Birth City": "",
                                "DST of Residence": ""
                            }
                            ]

        const jsonInfo = {};
        jsonData.forEach((student) => {
            const name = student.Grade;

            if (jsonInfo[name]) {
                jsonInfo[name].value++;
            } else {
                jsonInfo[name] = { name: name, value: 1 };
            }
        });
        const data = Object.values(jsonInfo);

        // continue with chart
        const color = d3.scaleOrdinal()
            .domain(data)
            .range(d3.schemeSet2);

        const pie = d3.pie()
            .sort(null)
            .value(d => d.value);

        const arc = d3.arc()
            .innerRadius(0)
            .outerRadius(Math.min(width, height) / 2 - 1);

        const labelRadius = arc.outerRadius()() * 0.8;

        const arcLabel = d3.arc()
            .innerRadius(labelRadius)
            .outerRadius(labelRadius);

        const arcs = pie(data);

        const svg = d3.select("#my_dataviz")
            .attr("width", width)
            .attr("height", height)
            .attr("viewBox", [-width / 2, -height / 2, width, height])
            .attr("style", "max-width: 100%; height: auto; font: 18px sans-serif;");

        svg.append("g")
            .attr("stroke", "white")
            .selectAll()
            .data(arcs)
            .join("path")
            .attr("fill", d => color(d.data.name))
            .attr("d", arc)
            .append("title")
            .text(d => `${d.data.name}: ${d.data.value.toLocaleString("en-US")}`);

        svg.append("g")
            .attr("text-anchor", "middle")
            .selectAll()
            .data(arcs)
            .join("text")
            .attr("transform", d => `translate(${arcLabel.centroid(d)})`)
            .call(text => text.append("tspan")
                .attr("y", "-0.4em")
                .attr("font-weight", "bold")
                .text(d => d.data.name))
            .call(text => text.filter(d => (d.endAngle - d.startAngle) > 0.25).append("tspan")
                .attr("x", 0)
                .attr("y", "0.7em")
                .attr("fill-opacity", 0.7)
                .text(d => d.data.value.toLocaleString("en-US")));
    }
}
</script>  