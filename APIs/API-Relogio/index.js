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
    let time = hour+":"+minutes
    return res.json({hora:hour, minute:minutes})
})

//rota caso informe hora E minuto
app.get('/vinl/rest/clock/:hour/:minutes', (req, res) => {
    let hour = req.params.hour
    let minutes = req.params.minutes
    let time = hour+":"+minutes
    if(!minutes){
        minutes = 0
    }
    return res.json({hora:hour, minute:minutes})
})

app.listen(8080, () => {
    console.log('Server iniciado na porta 8080')
})