<script lang="ts" setup>
import { DataAnalysis, Document, Files, House, } from '@element-plus/icons-vue'
</script>

<template>
  <el-menu default-active="1" >
    <el-menu-item index="1">
      <el-icon>
        <House/>
      </el-icon>
      <span>Table only view</span>
    </el-menu-item>
    <el-menu-item index="2">
      <el-icon>
        <DataAnalysis/>
      </el-icon>
      <span>Overview</span>
    </el-menu-item>
    <el-menu-item index="3">
      <el-icon>
        <Document/>
      </el-icon>
      <span>CSV Central</span>
    </el-menu-item>
    <el-sub-menu index="4">
      <template #title>
        <el-icon>
          <Files/>
        </el-icon>
        <span>Other</span>
      </template>
      <el-menu-item-group title="Group One">
        <el-menu-item index="1-1">item one</el-menu-item>
        <el-menu-item index="1-2">item two</el-menu-item>
      </el-menu-item-group>
      <el-menu-item-group title="Group Two">
        <el-menu-item index="1-3">item three</el-menu-item>
      </el-menu-item-group>
      <el-sub-menu index="1-4">
        <template #title>item four</template>
        <el-menu-item index="1-4-1">item one</el-menu-item>
      </el-sub-menu>
    </el-sub-menu>
  </el-menu>
</template>

<style scoped>
/*
.el-menu .el-menu-item:hover, .el-menu-demo .el-sub-menu__title:hover {
  background-color: #ECF0E9;
}
 */
</style>