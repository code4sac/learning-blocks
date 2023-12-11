<script lang="ts" setup>
</script>

<template>
  <el-container direction="vertical">
    <div class="about">
      <h1>Demo of styles:</h1>
      <StyleDemoTable>
        <template #headers>
          <el-text size="small">Demo of text el-text</el-text>
          <el-text>Demo of text el-text</el-text>
          <el-text size="large">Demo of text el-text</el-text>
          <p>Demo of text p</p>
        </template>
      </StyleDemoTable>
    </div>
  </el-container>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>