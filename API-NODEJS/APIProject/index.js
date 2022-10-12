// 1- Criando as variáveis para armazenar as bibliotecas
const express = require('express')
const morgan = require('morgan')
const cors = require('cors')
const bodyParser = require('body-parser')

//2- Instanciar express
const app = express()

//3- Add os complementos ao projeto
app.use(morgan('dev'))//morgan ao projeto para que tenhamos o log de execução
app.use(bodyParser.urlencoded({ extended: false}))
app.use(express.json()) //serve para informar o tipo de dados que queremos receber, que no nosso caso será um JSON
app.use(cors())// para definir quem pode comunicar coma  api

//5- simulando DB
let db = [
    { '1': { Nome: 'Cliente 1', idade: '20'}},
    { '2': { Nome: 'Cliente 2', idade: '30'}},
    { '3': { Nome: 'Cliente 3', idade: '40'}}
]

//6- 
app.get('/', (req, res) => {
    return res.json(db)
})// sem caminho especifico, sendo somente a rota como caminho do get

//4- startando server
app.listen(8081, () => {
    console.log('Express iniciado em http://localhost:8081')
})