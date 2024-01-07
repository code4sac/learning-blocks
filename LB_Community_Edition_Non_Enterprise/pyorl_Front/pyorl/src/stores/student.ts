import {computed, ref} from 'vue'
import {defineStore} from 'pinia'

export const useStudentStore = defineStore('student', () => {
  const count = ref(0)
  const doubleStudent = computed(() => count.value * 2)

  function increment() {
    count.value++
  }

  return {count, doubleStudent, increment}
})
