<template>
    <div>
        <table :tableData = datatoDisplay 
               :headerData = headertoDisplay 
               border="1" 
               style="border-collapse: collapse;">
            <thead>
                <tr >
                    <th v-for="(header, i) in headertoDisplay" :key="i">
                        <TableHead>{{ header }}</TableHead>
                    </th>
                </tr>
            </thead>
            <tbody>
                <AGISRow v-for="(data,i) in datatoDisplay" 
                :key="i" 
                :student="data" 
                :index="i"
                @indexesUpdated="handleIndexUpdate"
                />
            </tbody>
        </table>
    </div>
</template>
<script setup lang="ts">
/* eslint-disable */

import {ref, toRefs,  watch, defineAsyncComponent } from 'vue';
import { EmittedValue } from "../../types/interfaces"
const TableHead = defineAsyncComponent(()=> import("../TableComponents/TableHead.vue"));
const AGISRow = defineAsyncComponent(()=>import("../TableComponents/AGISRows.vue"))

    interface DisplayItems{
         AttendanceProgramCodePrimary: string;
         Grade: number;
         InactiveStatusCode: string;
         StudentID: number
    }
    const props = defineProps <{tableData: Array<DisplayItems>; headerData: Array<string>}>();
    const {tableData} = toRefs(props);
    const {headerData} = toRefs(props);

    const datatoDisplay = ref<Array<DisplayItems>>([]);
    const headertoDisplay = ref<Array<string>>([]);
    const emit = defineEmits<{(e:"grabIndexes",value: EmittedValue):void}>()
    

    watch(tableData,async () => {
        datatoDisplay.value = tableData.value;
        // console.log('tableData',tableData.value);
        
    })
    watch(headerData,async () => {
        headertoDisplay.value = headerData.value;
        // console.log('headerData', toRaw(headertoDisplay.value));
    })

    function handleIndexUpdate(payload: EmittedValue): void{
        emit('grabIndexes',{updatedIndexes:payload.updatedIndexes})
    }


</script>
