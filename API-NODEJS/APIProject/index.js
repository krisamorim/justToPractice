// 1- Criando as variáveis para armazenar as bibliotecas
const express = require('express')
const morgan = require('morgan')
const cors = require('cors')
const bodyParser = require('body-parser')

//8- Importando arquivo de rota
const routes = require('./Configs/routes')

//2- Instanciar express
const app = express()

// 3- Add os complementos ao projeto
app.use(morgan('dev'))//morgan ao projeto para que tenhamos o log de execução
app.use(bodyParser.urlencoded({ extended: false}))
app.use(express.json()) //serve para informar o tipo de dados que queremos receber, que no nosso caso será um JSON
app.use(cors())// para definir quem pode comunicar coma  api

//9- Configurar par ao app utilizar arquivo de rota
app.use(routes)


//5- simulando DB
let db = [
    { '1': { Nome: 'Cliente 1', idade: '20'}},
    { '2': { Nome: 'Cliente 2', idade: '30'}},
    { '3': { Nome: 'Cliente 3', idade: '40'}}
]

//6- sem caminho especifico, sendo somente a rota raiz como caminho do get
app.get('/', (req, res) => {
    return res.json(db)
})

//7- update
app.post('/add', (req, res) => {
    const body = req.body

    if(!body)
        return res.status(400).end()
        
    
    db.push(body)
    return res.json(body)
})

//4- startando server
app.listen(8081, () => {
    console.log('Server startado na porta 8081')
})