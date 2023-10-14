<script setup lang="ts">
import {ref} from 'vue';


const schoolcodeInput = ref<string>("");
const isvaildRange = ref<boolean>(true);
const studentIdInput = ref<string>("");

function validateSchoolCode(){
    const inrangeValue = !isNaN( Number(schoolcodeInput.value) ) && Number(schoolcodeInput.value) > 0 && Number(schoolcodeInput.value) <= 999 ;
    isvaildRange.value = (inrangeValue)?  true : false;  
}

</script>

<template>
    <form action="submit" @submit.prevent = "$emit('formOutput', [schoolcodeInput, studentIdInput])">

        <!-- <div>
            <label for="studentInfoSystems">Student Infromation System </label>
            <select> </select>
        </div> -->

        <div class="form-control" :class="{invalid: !isvaildRange}">
            <label for="schoolCode"> School Code</label>
            <input id="schoolCode" name="schoolCode"  type="text" v-model="schoolcodeInput" @change="validateSchoolCode " placeholder = "School Code..."  required/>
            <p v-if="!isvaildRange">Please enter valid School Code</p>
        </div> 

        <div >
            <label for="studentId"> Student ID</label>
            <input id="studentId" name="studentId"  type="text" v-model="studentIdInput"  placeholder = "Student ID..." />
        </div> 

        <div>
            <!-- Block form submition on invalid schoolCode -->
            <button type="submit" :disabled="!isvaildRange" >Search</button>
        </div>

    </form>
</template>

<style>
    form-control{
        margin: 0.5rem 0;
    }
    .form-control.invalid input{
        border: solid 1px red;
    }

</style>