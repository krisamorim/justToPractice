const express = require('express')
const morgan = require('morgan')
const app = express()
const queries = require('./src/data/queries.json')
app.use(morgan('dev'))

//rota para ler o json
app.get('/', (req, res) => {
    return res.json(queries)
})

//rota caso informe somente a hora
app.get('/vinl/rest/clock/:hour', (req, res) => {
    let hour = req.params.hour
    let minutes = "0"
    let tempo = hour+":"+minutes
    let querieFound = queries.find((querie) => {
        return querie.time === tempo;
    })
    //console.log("o time é: "+tempo)
    //console.log(querieFound)
    if(querieFound){
        var angulo = querieFound['angle']
    }else{
        //comadno para conectar
        //comando para achar
        //associar o valor achar a variavel angulo
        angulo = "buscar no DB"
        //add a nova consulta ao arquivo json
    }
    return res.json(angulo)
})

//rota caso informe hora E minuto
app.get('/vinl/rest/clock/:hour/:minutes', (req, res) => {
    let hour = req.params.hour
    let minutes = req.params.minutes
    let tempo = hour+":"+minutes
    let querieFound = queries.find((querie) => {
        return querie.time === tempo;
    })

    if(querieFound){
        var angulo = querieFound['angle']
    }else{
        //comadno para conectar
        //comando para achar
        //associar o valor achar a variavel angulo
        angulo = "buscar no DB"
        //add a nova consulta ao arquivo json
    }
    return res.json(angulo)
})

app.listen(8080, () => {
    console.log('Server iniciado na porta 8080')
})