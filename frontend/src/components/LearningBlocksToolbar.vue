<template>
 
  <v-app-bar :elevation="4" class="bg-blue-lighten-1">
    <template v-slot:prepend>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>
    </template>
    <v-app-bar-title style="cursor: pointer" @click="$router.push('/report')">
      Learning Blocks
    </v-app-bar-title>
    <v-spacer></v-spacer>
    

    <v-select v-model= "toggle_test"
    label="Student Information System"
   
   
    variant="underlined"
    >
    <option v=for = 'toggle_test in toggle_test'>{{toggle_test}}</option>
    </v-select>
  </v-app-bar>

  
</template>

<script>
export default {
  name: "LearningBlocksToolbar",
  data: () => ({
    
    toggle_test: ['Aeries', 'ALMA (TBD)'],
    
    
    
    links: [
      'Home',
      'About Us',
      'Team',
      'Services',
      'Blog',
      'Contact Us',
    ],
    
    
    
    
  }),
}
</script>

<style scoped>

</style>
