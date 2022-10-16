const fs = require('fs')
const filePath = './src/data/teste.json'
const fileOriginal = require('./src/data/teste.json') 
let file = fileOriginal
console.log(file)

file.push({ time: "2:0", angle: 60 })


function save(data){
    const convertToString = JSON.stringify(data)
    return fs.writeFileSync(filePath, convertToString)
}

save(file)
console.log(fileOriginal)