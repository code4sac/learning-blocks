<script lang="ts" setup>
import { More, } from '@element-plus/icons-vue'

const data1 = [
  {statisticName: 'Total', statisticNumber: 3897},
  {statisticName: 'Female', statisticNumber: 3897},
  {statisticName: 'Male', statisticNumber: 3897},
  {statisticName: 'Asian', statisticNumber: 3897},
]
const data2 = [
  {statisticName: 'Native American', statisticNumber: 3897},
  {statisticName: 'Black', statisticNumber: 3897},
  {statisticName: 'Hispanic', statisticNumber: 3897},
  {statisticName: 'White', statisticNumber: 3897},
]

const doClick = () => {
  console.log('aaaaaa')
}

const doClick2 = () => {
  console.log('bbbbbb')
}
</script>

<template>
  <div class="statistic-outer-container">
    <div class="statistic-inner-container">
      <div class="menu-section">
        <el-dropdown trigger="click">
          <span class="el-dropdown-link">
            <el-icon class="more-icon">
              <More/>
            </el-icon>
          </span>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item>Action 1</el-dropdown-item>
              <el-dropdown-item>Action 2</el-dropdown-item>
              <el-dropdown-item>Action 3</el-dropdown-item>
              <el-dropdown-item disabled>Action 4</el-dropdown-item>
              <el-dropdown-item divided>Action 5</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </div>
      <el-row :gutter=24 justify="center">
        <el-col v-for="item in data1" :key="item.statisticName" :span="6">
          <el-card>
            <el-statistic :value="item.statisticNumber" @click="doClick2">
              <template #title>
                <div>
                  {{ item.statisticName }}
                  <el-dropdown style="margin-left: 4px" trigger="click">
                    <span class="el-dropdown-link">
                      <el-icon class="more-icon">
                        <More/>
                      </el-icon>
                    </span>
                    <template #dropdown>
                      <el-dropdown-menu>
                        <el-dropdown-item>Action 1</el-dropdown-item>
                        <el-dropdown-item>Action 2</el-dropdown-item>
                        <el-dropdown-item>Action 3</el-dropdown-item>
                        <el-dropdown-item disabled>Action 4</el-dropdown-item>
                        <el-dropdown-item divided>Action 5</el-dropdown-item>
                      </el-dropdown-menu>
                    </template>
                  </el-dropdown>
                </div>
              </template>
            </el-statistic>
          </el-card>
        </el-col>
      </el-row>
      <el-row :gutter=24 justify="center">
        <el-col v-for="item in data2" :key="item.statisticName" :span="6">
          <el-card>
            <el-statistic :value="item.statisticNumber" @click="doClick2">
              <template #title>
                <div>
                  {{ item.statisticName }}
                  <el-dropdown style="margin-left: 4px" trigger="click">
                    <span class="el-dropdown-link">
                      <el-icon class="more-icon">
                        <More/>
                      </el-icon>
                    </span>
                    <template #dropdown>
                      <el-dropdown-menu>
                        <el-dropdown-item>Action 1</el-dropdown-item>
                        <el-dropdown-item>Action 2</el-dropdown-item>
                        <el-dropdown-item>Action 3</el-dropdown-item>
                        <el-dropdown-item disabled>Action 4</el-dropdown-item>
                        <el-dropdown-item divided>Action 5</el-dropdown-item>
                      </el-dropdown-menu>
                    </template>
                  </el-dropdown>
                </div>
              </template>
            </el-statistic>
          </el-card>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<style scoped>
.el-col {
  text-align: center;
  max-width: 300px;
}

.el-row {
  padding: 8px 0;
}

.statistic-outer-container {
  display: flex;
  justify-content: center;
}

.statistic-inner-container {
  max-width: 1200px;
  flex-grow: 1;
}

.menu-section {
  display: flex;
  justify-content: end;
}

.more-icon {
  cursor: pointer;
}
</style>
