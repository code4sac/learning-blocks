<script lang="ts" setup>
import WelcomeItem from './WelcomeItem.vue'
</script>

<template>
  <WelcomeItem>
    <template #icon>
      <el-image src="/welcome_block_02.png"/>
    </template>
    <template #heading>Feature 1</template>

    Vue’s
    <a href="https://vuejs.org/" rel="noopener" target="_blank">official documentation</a>
    provides you with all information you need to get started.
  </WelcomeItem>

  <WelcomeItem style="padding-top: 1rem">
    <template #icon>
      <el-image src="/welcome_block_03.png"/>
    </template>
    <template #heading>Compare student data with State of California standards</template>
    <el-link>Dashboard ➜ CA Data</el-link>
    Visualize student data relative to defined State of California educational benchmarks for actionable insights.
  </WelcomeItem>

  <WelcomeItem style="padding-top: 1rem">
    <template #icon>
      <el-image src="/welcome_block_04.png"/>
    </template>
    <template #heading>Download a CSV file based on filter of students</template>
    <el-link>Interventions ➜ Downloads</el-link>
    Use precise student filters to refine and generate focused data in CSV format.
  </WelcomeItem>

  <WelcomeItem style="padding-top: 1.2rem">
    <template #icon>
      <el-image src="/welcome_block_05.png"/>
    </template>
    <template #heading>Feature 4</template>

    Vue’s
    <a href="https://vuejs.org/" rel="noopener" target="_blank">official documentation</a>
    provides you with all information you need to get started.
  </WelcomeItem>

  <WelcomeItem style="padding-top: 1rem">
    <template #icon>
      <el-image src="/welcome_block_06.png"/>
    </template>
    <template #heading>View Learning Blocks on GitHub</template>

    <el-link href="https://github.com/code4sac/learning-blocks">Code repository on GitHub.com</el-link>
    This project is open-source, and made by volunteers at Open Sacramento.
  </WelcomeItem>
</template>

<style scoped>
</style>