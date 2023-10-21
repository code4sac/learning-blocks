<template>
    <div>
        <h4>Result</h4>
        <div class="search-container">
            <input type= "text" v-model = "searchText" class="search-input" placeholder="Search..." >
            <v-btn class="search-padding-left" @click="enrollmentSearch">Search</v-btn>
        </div>
        <div>
            <v-btn @click="buttonDownload">
                Download
            </v-btn>
        </div>
        <aries-data-table :data-column-headers="enrollmentCardColumnHeaders" :data-rows="enrollmentCardRows">
        </aries-data-table>
    </div>
</template>
<style>
    .search-input::placeholder{
        color: #232222;
    }
    .search-container{
        padding-bottom: 10px;
    }
    .search-padding-left{
        left:10px;
        padding-left: 15px;
    }
</style>

<script>
    import AriesDataTable from '@/components/AriesDataTable.vue'    

    import { createCSVDownload } from '@/lib/CsvParser'
    export default {
        name: 'enrollmentDetails',
        components: {AriesDataTable},

        data: () =>({

            leftMostIndex: null,
            rightMostIndex: null,
            SearchResultsArray: [],
            searchText: '',
            queryFields:'',
            apiKey: '',
            tableData:{
                type: Array,
                default: () =>{
                    return [{
                        'StudentID': 0,
                        'SchoolCode': 0,
                        "LastName": "",
                        "FirstName": "",
                        "Gender": "",
                        "Grade": 0,
                        "Birthdate": "",
                        "HomePhone": "",
                        "ResidenceAddress": "",
                        "ResidenceAddressCity": "",
                        "ResidenceAddressState": "",
                        "ResidenceAddressZipCode": "",
                    }]
                }
            }
        }),
  
        methods:{
            enrollmentSearch(){
                if(this.SearchResultsArray.length > 0){
                    this.SearchResultsArray.splice(0,this.SearchResultsArray.length)
                }
                this.leftmostBinarySearch(this.tableData,this.searchText)
                this.rightmostBinarySearch(this.tableData,this.searchText)
                this.populateSearchArray(this.tableData)
            },
            buttonDownload(){
                createCSVDownload(this.SearchResultsArray,'','Enrollment')
            },
            leftmostBinarySearch(data,target){
                let left = 0
                let right = data.length -1
                while(left < right){
                    const mid  = Math.floor((left + right) /2)
                    if(String( data[mid]['LastName']).toLowerCase() < target.toLowerCase()){
                        left = mid + 1
                    }
                    else{
                        right = mid
                    }
                }
                if(String(data[left]['LastName']).toLowerCase() === target.toLowerCase()){
                    this.leftMostIndex = left
                }
                else{
                    this.leftMostIndex = -1
                }
            },
            rightmostBinarySearch(data,target){
                let left = 0
                let right = data.length
                while(left < right){
                    const mid = Math.floor((left + right)/2)
                    if(String( data[mid]['LastName']).toLowerCase() > target.toLowerCase()){
                        right = mid
                    }
                    else{
                        left = mid + 1
                    }
                }
                if(String(data[right-1]['LastName']).toLowerCase() === target.toLowerCase()){
                    this.rightMostIndex = right - 1
                }
                else{
                    this.rightMostIndex = -1
                }
            },
            populateSearchArray(data){
                if(this.leftMostIndex < 0 && this.rightMostIndex < 0){
                    console.log("NO RESULTS WHERE FOUND")
                    return
                }
                for(let i = this.leftMostIndex; i <= this.rightMostIndex; i++){
                    this.SearchResultsArray.push(data[i])
                }
                console.log(this.SearchResultsArray)
            }
        },
        computed:{
            enrollmentCardColumnHeaders(){
                return Object.keys(this.SearchResultsArray[0])
            },
            enrollmentCardRows(){
                return this.SearchResultsArray.reduce((accumulator, currentValue) => [...accumulator, Object.values(currentValue)], [])
            }

        },
        created() {
            this.tableData = JSON.parse(localStorage.getItem(this.$route.params.localStorageKey))
            console.log(this.tableData)
            
           
            this.leftmostBinarySearch(this.tableData,'Garcia')
            this.rightmostBinarySearch(this.tableData,'Garcia')
            this.populateSearchArray(this.tableData)

        }

        
    }

</script>