<script lang="ts" setup>
import IconNotice from "@/components/icons/IconNotice.vue";
import { reactive } from 'vue'
import { ElCheckbox, ElFormItem, ElInput } from "element-plus";
import TheWelcome from "@/components/TheWelcome.vue";
import { QuestionFilled } from "@element-plus/icons-vue"
import AppFooter from "@/components/app/AppFooter.vue";

const formInline = reactive({
  user: '',
  checked: false,
  region: '',
  date: '',
})
const onSubmit = () => {
  console.log('submit!')
}
</script>

<template>
  <el-container>
    <el-main>
      <el-row>
        <el-col :md="12" class="left_section_container">
          <h1>
            <el-text style="font-size: var(--el-font-size-extra-large);">Welcome to Learning Blocks.</el-text>
          </h1>
          <el-text>Unleash your school power: Parents, students, and admins, unlock grades, schedules, and progress in
            one thrilling platform! ✨
          </el-text>
          <div>
            <el-text class="notice">
              <el-icon :size="20" style="margin-right: 28px">
                <IconNotice/>
              </el-icon>
              <ul>
                <li>All your data stays private in your browser - Learning Blocks never saves it online.</li>
                <li>Learning Blocks saves progress locally. What you sync stays on your device.</li>
              </ul>
            </el-text>
          </div>
          <div class="getting_started_container">
            <h2>
              <el-text style="font-size: var(--el-font-size-extra-large);">Getting Started:</el-text>
            </h2>
            <ul class="list">
              <li style="padding-top: 10px">
                <el-card>
                  <h3>
                    <el-text size="large">1. Step One</el-text>
                  </h3>
                  <div style="padding-top: .5em">
                    <el-text>
                      <ul class="list_bullet">
                        <li> Ready with your API key? Sync it now for seamless access!
                        </li>
                        <li> No API key yet, or prefer a different option? Simply skip to Step 2!
                        </li>
                      </ul>
                    </el-text>
                  </div>
                  <div class="documentation_notice_container">
                    <el-text type="info">
                      <el-icon :size="24">
                        <QuestionFilled/>
                      </el-icon>
                      For help, visit the handy
                      <el-link href="#">help page</el-link>
                      .
                    </el-text>
                  </div>
                  <div class="sync_api_key_container">
                    <el-form :inline="true" :model="formInline" class="demo-form-inline">
                      <el-form-item label="Sync API Key">
                        <el-input v-model="formInline.user" :disabled="formInline.checked" clearable
                                  placeholder="API Key"/>
                      </el-form-item>
                      <el-checkbox v-model="formInline.checked" label="Use Demo Data" size="large"/>
                      <el-form-item style="margin-left: 1em">
                        <el-button type="primary" @click="onSubmit">Sync</el-button>
                      </el-form-item>
                    </el-form>
                  </div>
                </el-card>
              </li>
              <li style="padding-top: 10px">
                <el-card>
                  <h3>
                    <el-text size="large">2. Step Two</el-text>
                  </h3>
                  <div style="padding-top: .5em">
                    <el-text>
                      Get the big picture of the school year! Our
                      <el-link href="/dashboard">dashboard</el-link>
                      lets you explore public data – grades, attendance, and more – instantly. Want even deeper
                      insights? Connect with your school's API for a truly personalized view. Learn more
                      <el-link>here</el-link>
                      .
                    </el-text>
                    <div style="padding: .5em 0">
                      <a class="el-button el-button--primary" href="/dashboard" style="text-decoration: none;">Go to
                        Dashboard</a>
                    </div>
                  </div>
                  <div style="padding-top: .5em">
                    <el-image src="/docs_screenshot_01.png"/>
                  </div>
                </el-card>
              </li>
            </ul>
          </div>
        </el-col>
        <el-col :md="12" class="right_section_container">
          <TheWelcome></TheWelcome>
        </el-col>
      </el-row>
    </el-main>
    <el-footer>
      <AppFooter></AppFooter>
    </el-footer>
  </el-container>
</template>

<style scoped>
* {
    word-break: normal;
}
@media (min-width: 991px) {
  .left_section_container {
    padding-right: 2rem;
  }
}

.getting_started_container {
  padding-top: 10px
}

.right_section_container {

}

.sync_api_key_container {
  padding: 20px 0;
}

.documentation_notice_container {
  padding: 16px 0;
}

.notice {
  padding: 12px;
  display: flex;
}

.list_bullet {
  list-style-position: inside;
}

.list {
  list-style: none;
}

.demo-form-inline {
  display: inline;

  .el-input {
    --el-input-width: 220px;
  }
}

</style>
