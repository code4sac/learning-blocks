<script>
import * as d3 from 'd3'
import {computed} from 'vue';

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
    const width = 450,
      height = 300;

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

    const radius = Math.min(width, height) / 2;

    const svg = d3.select(`#${this.containerId}`).append("svg")
      .attr("width", width)
      .attr("height", height)
      .attr("viewBox", [-width / 2, -height / 2, width, height])
      .attr("style", "max-width: 100%; height: auto; font: 18px sans-serif;");

    svg.append("g")
      .selectAll()
      .data(arcs)
      .join("path")
      .attr("fill", d => color(d.data.name))
      .attr("d", arc)

    svg
      .selectAll('allPolylines')
      .data(arcs)
      .enter()
      .append('polyline')
      .attr('stroke', 'black')
      .style('fill', 'none')
      .attr('stroke-width', 1)
      .attr('points', (d) => {
        const posA = arc.centroid(d)
        const posB = arcLabel.centroid(d) // line break
        const posC = arcLabel.centroid(d); // Label position
        const midangle = d.startAngle + (d.endAngle - d.startAngle) / 2 // angle of X pos extreme right or extreme left
        posC[0] = radius * 0.95 * (midangle < Math.PI ? 1 : -1); // 1 or -1 = right or left
        return [posA, posB, posC]
      })

    svg.append("g")
      .selectAll()
      .data(arcs)
      .enter()
      .append('text')
      .text(  (d) => { return `${d.data.name} (${d.data.value})` } )
      .attr('transform', (d) => {
        const pos = arcLabel.centroid(d);
        const midAngle = d.startAngle + (d.endAngle - d.startAngle) / 2
        pos[0] = radius * 0.99 * (midAngle < Math.PI ? 1 : -1);
        return `translate(${  pos  })`;
      })
      .style('text-anchor', (d) => {
        const midAngle = d.startAngle + (d.endAngle - d.startAngle) / 2
        return (midAngle < Math.PI ? 'start' : 'end')
      })
  }
}
</script>
  
<template>
    <div>
        <div :id="containerId" class="pieContainer"></div>
        <p>{{ chartLabel }}</p>
    </div>
</template>

<style>
  .pieContainer{
    width: 400px;
  }
</style>