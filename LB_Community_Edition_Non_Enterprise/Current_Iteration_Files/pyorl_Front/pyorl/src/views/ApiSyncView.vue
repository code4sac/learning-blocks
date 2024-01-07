<script lang="ts" setup>
import StudentRecord from "@/components/StudentRecord.vue";
import IconWarning from "@/components/icons/IconWarning.vue";
</script>

<template>
  <el-container>
    <el-main>
      <div class="sync_status_container">
        <el-icon :size="24">
          <IconWarning/>
        </el-icon>
        <el-text type="warning">You are currently not synced with the API.</el-text>
        <br>
        <br>
      <el-text>Once there is an API connection, the results will show up below.</el-text>
      </div>
      <StudentRecord/>
    </el-main>
    <el-footer></el-footer>
  </el-container>
</template>

<style scoped>
.sync_status_container {
  padding: 20px 0 30px 0;
}
</style>