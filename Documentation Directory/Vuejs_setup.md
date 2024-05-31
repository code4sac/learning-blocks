Setting the frontend:

1. Open terminal window
2. Enter "npm init vue@latest" then follow the
   instruction. [Enter the project name, and the packages you'd like to have installed]
3. If projectname is `fastapivue`, then Enter `cd fastapivue` to change directory to the directory of the project.
4. Enter `npm install`,  `npm install axios`, `npm run dev`

Writing Code:

Open HelloWord.vue component.
add:
<script>
export default {
    data() {
        return {
            studentsRecord: null,
        }
    },
    methods: {
        fetchStudentsRecord() {
            const URL = `https://demo.aeries.net/aeries/api/v5/enrollment/99400001/year/2020cert=477abe9e7d27439681d62f4e0de1f5e1`
            // api key = 477abe9e7d27439681d62f4e0de1f5e1
            // url = https://demo.aeries.net/aeries/api/v5/schools/994/students/99400001
        }
    }
}
</script>

## more documentation soon

<img align="right" alt="GIF" src="https://i.pinimg.com/originals/e4/26/70/e426702edf874b181aced1e2fa5c6cde.gif" />
