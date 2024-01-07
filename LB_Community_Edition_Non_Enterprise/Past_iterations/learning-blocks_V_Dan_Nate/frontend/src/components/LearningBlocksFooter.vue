<template>
  <v-footer class="bg-blue-lighten-1">
    <v-row justify="center" no-gutters>
      <v-btn
          v-for="link in links"
          :key="link"
          class="mx-2"
          color="white"
          rounded="xl"
          variant="text"
      >
        {{ link }}
      </v-btn>
      <v-col class="text-center mt-4" cols="12">
        {{ new Date().getFullYear() }} — <strong>Learning Blocks</strong>
      </v-col>
    </v-row>
  </v-footer>

</template>

<script>
export default {
  name: "AppToolbar"
}
</script>

<style scoped>

</style>