<script lang="ts" setup>
import {ref} from 'vue'

const activeIndex = ref('1')
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>

<template>
  <el-menu
    :default-active="activeIndex"
    :ellipsis="false"
    active-text-color="#426B1F"
    class="el-menu-demo"
    mode="horizontal"
    text-color="#000"
    @select="handleSelect"
  >
    <div class="left-item">
      <img
        alt="Element logo"
        src="/logo_lb_red_03.png"
      />
    </div>
    <div class="flex-grow"/>
    <el-menu-item index="1">
      <RouterLink to="/">Home</RouterLink>
    </el-menu-item>
    <el-menu-item index="2">Dashboard</el-menu-item>
    <el-menu-item index="3">
      <RouterLink to="/graph">Graph</RouterLink>
    </el-menu-item>
    <el-menu-item index="4">
      <RouterLink to="/student-record">Student Record</RouterLink>
    </el-menu-item>
    <el-menu-item index="5">
      <RouterLink to="/about">About</RouterLink>
    </el-menu-item>
  </el-menu>
</template>

<style scoped>
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

</style>
