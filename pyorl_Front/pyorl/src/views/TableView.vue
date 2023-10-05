<template>
    <Transition v-if="!hideForm">
      <FromInput @formOutput ="(payload) => 
        { schoolcodeValue = payload[0]; studentID = payload[1];}">
      </FromInput>
    </Transition>
  
    <Transition>
      <DisplayTable :tableData = "studentRequst" 
                    :headerData="headerDisplay"
                    @grabIndexes="grabSelectedRows"
                    >
      </DisplayTable>
      
    </Transition>
    <button @click="generateFiles">
      Download
    </button>
    
  </template>
  
  <script setup lang="ts">
    import { ref, watch, toRaw, defineAsyncComponent} from 'vue';
    import { EmittedValue } from '@/types/interfaces';
    import axios from 'axios';
    const FromInput = defineAsyncComponent(()=> import("../components/FormInputs/FormInput.vue"));
    const DisplayTable = defineAsyncComponent(()=> import("../components/TableComponents/DisplayTable.vue"));
    
  
    
  
    interface DisplayItems{
      AttendanceProgramCodePrimary: string;
      Grade: number;
      InactiveStatusCode: string;
      StudentID: number
    }
  
    const schoolcodeValue = ref<string>("");
    const studentID = ref<string>("");
    const hideForm = ref<boolean>(false);
    const studentRequst = ref<Array<DisplayItems>>([]);
    const headerDisplay = ref<Array<string>>([]);
    const selectedIndexes = ref<number[]>([]);
    
   
    watch(schoolcodeValue, async(schoolcodeValue) =>{
      try{
        const request = axios.get('http://127.0.0.1:8000/students/'
        .concat(schoolcodeValue));
  
        studentRequst.value = toRaw((await request).data[0]);
        headerDisplay.value = toRaw((await request).data[1]);
        hideForm.value = (studentRequst.value.length > 0) ? true: false;      
        
      }
      catch(err){
        console.log("ERROR",err)
  
      }
    })
    function grabSelectedRows(payload: EmittedValue){
      
      if(!selectedIndexes.value.includes(payload.updatedIndexes)){
          selectedIndexes.value.push(payload.updatedIndexes);
      }else{
          selectedIndexes.value = selectedIndexes.value.filter((item)=> item !== payload.updatedIndexes);
      }
  
      console.log(selectedIndexes.value);
      console.log(studentRequst.value.at(payload.updatedIndexes))
    }
    function generateFiles(){
      
    }
  
  
  </script>
  
  