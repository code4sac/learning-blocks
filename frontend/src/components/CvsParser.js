
export function exportDataFromJSON(data, fileName = "test.csv"){
    const csvString = transformToCSV(data)
    const blob = new Blob([csvString], {type: 'text/csv'})
    const url = window.URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.setAttribute('href',url)
    link.setAttribute('download',fileName)
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
}
   
function transformData(data, csvArr = []){
    const isObject = (object) => object != null && object.constructor.name === "Object"
    Object.keys(data).forEach(key =>{
        
        if(isObject(data[key]) || Array.isArray(data[key]) ){
            if(!isObject(Object.values(data[key]))  ){
                for(let i =0; i < Object.values(data[key]).length; i++){

                    if((Number.isInteger(Object.values(data[key])[i])) || (typeof Object.values(data[key])[i] === 'string') ){
                        let result = {}
                        result[Object.keys(data[key])[i]] = Object.values(data[key])[i]
                        csvArr.push(result)
                    }
                }
            }
            transformData(data[key],csvArr)
        }
    })
    return csvArr
}

function transformToCSV(data){
   
    const objects = transformData(data)

    const headers = []
    for(let i = 0; i < 7; i++){
        headers.push(Object.keys(objects[i]).join(','))
    }
  

    const rows = []
    for(let j = 0; j < objects.length; j++){
        if(j % 7 == 0){
            if(Object.keys(objects[j]) !=  headers[0]){
                rows.push(Object.values(objects[0]).join(','))
            }
        }
        rows.push(Object.values(objects[j]).join(','))
    }

    
    let csvString = headers.join(',') 
    for(let k = 0; k < rows.length; k++){
        if(k % 7 == 0){
            csvString += '\n'
        }
        const tmp = rows[k] + ','
        csvString += tmp
    }
    console.log(csvString)
    return csvString
}

