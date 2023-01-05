<template>
  <v-container>
    <h1 class="header center orange-text">Aries Report Cards</h1>
    <h5 class="header col s12 light">Find student data and download reports within the Aries school system</h5>
    <v-btn>Learn more</v-btn>
  </v-container>
  <v-form>
    <v-container>
      <v-row>
        <v-col cols="12" md="4">
          <v-text-field
              v-model="schoolId"
              label="School ID"
              required
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="4">
          <v-text-field
              v-model="studentId"
              label="Student ID"
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="4">
          <v-text-field
              v-model="apiKey"
              label="API Key"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-switch v-model="productionApi" label="Production API"></v-switch>
      <br>
      <v-btn type="submit" color="blue" @click.stop.prevent="submit">Generate query</v-btn>
    </v-container>
  </v-form>
</template>

<script>
export default {
  data: () => ({
    name: '',
    phoneNumber: '',
    email: '',
    select: null,
    items: [
      'Item 1',
      'Item 2',
      'Item 3',
      'Item 4',
    ],
    checkbox: null,
    productionApi: false,
    schoolId: '994',
    studentId: '99400002',
    apiKey: '477abe9e7d27439681d62f4e0de1f5e1',
  }),

  methods: {
    submit() {
      fetch(`http://127.0.0.1:3000/LearningBlocksAPI/demoAriesReportCard?api_type=demo&school_id=994&student_id=99400002&api_key=477abe9e7d27439681d62f4e0de1f5e1`);
      this.$router.push(`/report`);
    },
  //   clear() {
  //     this.name = ''
  //     this.phoneNumber = ''
  //     this.email = ''
  //     this.select = null
  //     this.checkbox = null
  //     this.$refs.observer.reset()
  //   },
  },
}
</script>