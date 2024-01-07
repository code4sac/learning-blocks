<template>
  <v-app :theme="theme">
    <learning-blocks-toolbar/>
    <v-main>
      <v-container fluid>
        <router-view/>
      </v-container>
    </v-main>
    <learning-blocks-footer/>
  </v-app>
</template>

<script setup>
import {ref} from 'vue'

const theme = ref('light')
</script>
<script>
import LearningBlocksToolbar from "@/components/LearningBlocksToolbar.vue";
import LearningBlocksFooter from "@/components/LearningBlocksFooter.vue";

export default {
  components: {
    LearningBlocksToolbar,
    LearningBlocksFooter
  }
}
</script>