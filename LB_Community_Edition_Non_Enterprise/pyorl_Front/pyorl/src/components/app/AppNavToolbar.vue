<script lang="ts" setup>
import { paths } from '@/router'
import { ElMenu, ElMenuItem } from "element-plus";
</script>

<template>
  <el-menu
      :default-active="$route.path"
      :ellipsis="false"
      :router="true"
      active-text-color="red"
      class="el-menu-demo"
      mode="horizontal">
    <div class="left-item">
      <a href="/" style="padding: 0; margin: 0; text-decoration: none;">
        <img
        alt="Element logo"
        src="/logo_lb_red_03.png"
      />
      </a>
    </div>
    <div class="flex-grow"/>
    <el-menu-item :index="paths.home">Home</el-menu-item>
    <el-menu-item :index="paths.dashboard">Dashboard</el-menu-item>
    <el-menu-item :index="paths.apiSync">API Sync 🚧Under Construction🚧</el-menu-item>
    <el-menu-item :index="paths.interventions">Interventions</el-menu-item>
  </el-menu>
</template>

<style scoped>
a img {
  display: block;
}
.left-item {
  padding-left: 20px;
  padding-right: 20px;
  display: flex;
  align-items: center;
}

.flex-grow {
  flex-grow: 1;
}

.left {
  display: inline;
  width: 300px;
  max-width: 300px;
}

.right {
  display: inline;
}

.el-menu-demo {
  --el-menu-active-color: #436a27;
}

.el-menu-demo .el-menu-item:hover, .el-menu-demo .el-sub-menu__title:hover {
  background-color: #ECF0E9;
  color: #436a27;
}
</style>
