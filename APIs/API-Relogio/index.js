const express = require('express')
const morgan = require('morgan')
const app = express()
const queries = require('./src/data/queries.json')
app.use(morgan('dev'))


//função para encontrar o angulo
function findAngule(h,m){
    let desiredTime = h + ":" + m
    let querieFound = queries.find((querie) => {
        return querie.time === desiredTime;
    })

    //verifica se a hora ja foi pesquisada
    if(querieFound){
        return querieFound['angle']
    }else{ //se não foi pesquisada pegue no db e coloque no json
        //comadno para conectar
        //comando para achar no DB
        //select angle from tabledefault t where "hour" = h and "minute" = m;
            //se não achar na DB
                //então calcular
                //add a base de dados
                //add ao arquivo queri
            //se achar ele faz o select e pega o angulo 
                //add ao arquivo querri
        //associar o valor achar a variavel angulo p/ mostra no navegador
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

    return res.json(findAngule(hour, minutes))
})

//rota caso informe hora E minuto
app.get('/vinl/rest/clock/:hour/:minutes', (req, res) => {
    let hour = req.params.hour
    let minutes = req.params.minutes
    return res.json(findAngule(hour,minutes))
})

app.listen(8080, () => {
    console.log('Server iniciado na porta 8080')
})