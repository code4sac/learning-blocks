<script lang="ts" setup>
import AppStatistic from "@/components/app/AppStatistic.vue";
</script>

<template>
  <main>
    <el-container>
      <el-header>
        <AppStatistic></AppStatistic>
      </el-header>
      <el-main>
        <el-aside class="sidebar">
          <AppNavSide></AppNavSide>
        </el-aside>
      </el-main>
      <el-footer>
      </el-footer>
    </el-container>
  </main>
</template>

<style scoped>
/*

 */
.sidebar {
  max-width: 256px;
}
</style>