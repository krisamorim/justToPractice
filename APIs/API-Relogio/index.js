const express = require('express')
const morgan = require('morgan')
const app = express()
const queries = require('./src/data/queries.json')
app.use(morgan('dev'))


//função para encontrar o angulo
function findAngule(desiredTime){
    let querieFound = queries.find((querie) => {
        return querie.time === desiredTime;
    })

    //verifica se a hora ja foi pesquisada
    if(querieFound){
        return querieFound['angle']
    }else{ //se não foi pesquisada pegue no db e coloque no json
        //comadno para conectar
        //comando para achar
        //associar o valor achar a variavel angulo
        return "buscar no DB"
        //add a nova consulta ao arquivo json
    }
}

//rota defaul para ler o json
app.get('/', (req, res) => {
    return res.json(queries)
})

//rota caso informe somente a hora
app.get('/vinl/rest/clock/:hour', (req, res) => {
    let hour = req.params.hour
    let minutes = "0"
    let tempo = hour+":"+minutes

    return res.json(findAngule(tempo))
})

//rota caso informe hora E minuto
app.get('/vinl/rest/clock/:hour/:minutes', (req, res) => {
    let hour = req.params.hour
    let minutes = req.params.minutes
    let tempo = hour+":"+minutes
    return res.json(findAngule(tempo))
})

app.listen(8080, () => {
    console.log('Server iniciado na porta 8080')
})