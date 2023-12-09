export function createCSVDownload(data, fileName = '', viewPathCall = '') {
  switch (viewPathCall) {
    case 'ReportCard': {
      const headerLength = 7
      getDownload(data, headerLength, fileName)
      break;
    }
    case 'Enrollment': {
      const headerLength = Object.keys(data[0]).length
      getDownload(data, headerLength, fileName)
      break;
    }
    case 'StudentsDetail': {
      const headerLength = Object.keys(data[0]).length
      getDownload(data, headerLength, fileName)
      break;
    }
    default: {
      console.log('Error ViewPathCall was not declared')
      break;
    }
  }
}

function getDownload(data, headerLength, fileName = "test.csv") {
  const csvString = transformToCSV(data, headerLength)
  const blob = new Blob([csvString], {type: 'text/csv'})
  const url = window.URL.createObjectURL(blob)
  const link = document.createElement('a')
  link.setAttribute('href', url)
  link.setAttribute('download', fileName)
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
}

function transformToCSV(data, headerLength) {
  const objects = transformData(data)
  const headers = []
  for (let i = 0; i < headerLength; i++) {
    headers.push(Object.keys(objects[i]).join(','))
  }
  const rows = []
  for (let j = 0; j < objects.length; j++) {
    if (j % headers.length == 0) {
      if (Object.keys(objects[j]).join(',') != headers[0]) {
        rows.push(Object.values(objects[0]).join(','))
      }
    }
    rows.push(Object.values(objects[j]).join(','))
  }
  let csvString = headers.join(',')
  for (let r = 0; r < rows.length; r++) {
    if (r % headers.length == 0) {
      csvString += '\n'
    }
    const tmp = rows[r] + ','
    csvString += tmp
  }
  console.log(csvString)
  return csvString
}

export function transformData(data, csvArr = []) {
  if (data === undefined || data.length == 0) return
  const isObject = (object) => object != null && object.constructor.name === "Object"
  Object.keys(data).forEach(key => {
    if (isObject(data[key]) || Array.isArray(data[key])) {
      if (!isObject(Object.values(data[key]))) {
        for (let i = 0; i < Object.values(data[key]).length; i++) {

          if ((Number.isInteger(Object.values(data[key])[i])) || (typeof Object.values(data[key])[i] === 'string')) {
            let result = {}
            result[Object.keys(data[key])[i]] = Object.values(data[key])[i]
            csvArr.push(result)
          }
        }
      }
      transformData(data[key], csvArr)
    }
  })
  return csvArr
}

// export function csvToJSON(data){
//     const object = transformToCSV(data)
//     const headers = object.slice(0, object.indexOf('\n')).split(',')
//     return object
//         .slice(object.indexOf('\n') + 1)
//         .split('\n')
//         .map(val =>{
//             const values = val.split(',')
//             return headers.reduce(
//                 (obj,header,index) => ((obj[header] = values[index]), obj),{}
//             )
//         })
// }