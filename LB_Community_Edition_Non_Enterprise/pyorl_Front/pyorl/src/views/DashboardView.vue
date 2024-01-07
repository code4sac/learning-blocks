<script lang="ts" setup>
import LearningBlocksToolbar from "@/components/app/AppPageHeader.vue";
import AppFooter from "@/components/app/AppFooter.vue";
</script>

<template>
  <el-container>
    <el-header>
      <LearningBlocksToolbar></LearningBlocksToolbar>
    </el-header>
    <el-main>
      <div>
        <!--        <EnrollmentDetails/>-->
      </div>
      <div>
        <!--        <ReportDetail/>-->
      </div>
    </el-main>
    <el-footer>
      <AppFooter></AppFooter>
    </el-footer>
  </el-container>
</template>