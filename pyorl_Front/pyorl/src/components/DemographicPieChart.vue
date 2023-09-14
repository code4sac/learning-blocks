<template>
    <div>
        <div :id="containerId" class="pieContainer"></div>
        <p>{{ chartLabel }}</p>
    </div>
</template>
  
<script>
import * as d3 from 'd3'
import { computed } from 'vue';

export default {
  props: {
    jsonData: {
      type: Object,
      required: true
    },
    containerId:{
        type: String,
        required: true
    }
  },
  setup(props){
    const propsId = computed(() => {
      if (props.containerId) {
        const words = props.containerId.split(/(?=[A-Z])/);
        return words[0];
      } else {
        return '';
      }
    });

    const chartLabel = computed(() => {
      return `Number of Students by ${propsId.value}`;
    });

    return {
        chartLabel
    };
  },
  mounted() {
    const width = 250,
      height = 250;

    const data = this.jsonData;

    const color = d3.scaleOrdinal()
      .domain(data.map(d => d.name))
      .range(d3.quantize(t => d3.interpolateSpectral(t * 0.8 + 0.1), data.length).reverse())

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

    const svg = d3.select(`#${this.containerId}`).append("svg")
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
      // Define the lower limit of when the frequency should be displayed at
      .call(text => text.filter(d => (d.endAngle - d.startAngle) > 0.27).append("tspan")
        .attr("x", 0)
        .attr("y", "0.7em")
        .attr("fill-opacity", 0.7)
        .text(d => d.data.value.toLocaleString("en-US")));
  }
}
</script>
  
<style>
  .pieContainer{
    width: fit-content;
  }
</style>