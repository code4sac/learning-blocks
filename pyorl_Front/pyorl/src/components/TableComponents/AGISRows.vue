<template>
    <tr @click = handleClick(props.index) 
        :class="{ 'highlight': selectedIndexes.includes(props.index) }">

        <td v-for="(field, i) in props.student" 
            :key="i" >{{ field }}</td>
    </tr>
</template>
<script setup lang="ts">
/* eslint-disable */
import {ref} from 'vue';
import {EmittedValue} from "../../types/interfaces"

interface DisplayItems{
         AttendanceProgramCodePrimary: string;
         Grade: number;
         InactiveStatusCode: string;
         StudentID: number
}
const props = defineProps<{ student: DisplayItems, index: number }>();
const selectedIndexes = ref<Array<number>>([]);

const emit = defineEmits<{(e:"indexesUpdated", 
                          value: EmittedValue): void}>()


function handleClick(index: number): void {
    if (!selectedIndexes.value.includes(index)) {
        selectedIndexes.value.push(index);
    } else {
        // If the index is already in the array, remove it
        selectedIndexes.value = selectedIndexes.value.filter((item) => item !== index);
    }
    emit('indexesUpdated',{updatedIndexes: index})
}

</script>
<style >
    .highlight {
        background-color: greenyellow;
    }
</style>