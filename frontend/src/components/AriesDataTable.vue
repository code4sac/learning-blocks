<template>
  <v-table>
    <thead>
    <tr>
      <th v-for="(header, i) in dataColumnHeaders" :key="i">{{ header }}</th>
    </tr>
    </thead>
    <tbody>
    <tr v-for="(row, i) in dataRows" :key="i">
      <td v-for="(field, i) in row" :key="i">{{ field }}</td>
    </tr>
    </tbody>
  </v-table>
</template>

<script>
export default {
  name: "AriesDataTable",
  props: {
    "dataColumnHeaders": {
      type: Array,
      default: () => ["SchoolID"]
    }, "dataRows": {
      type: Array,
      default: () => [["0"]]
    }
  },
  created() {
    console.log('')
  }
}
</script>

<style scoped>

</style>

