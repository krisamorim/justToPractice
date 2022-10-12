// 1- Criando as variáveis para armazenar as bibliotecas
const express = require('express')
const morgan = require('morgan')
const cors = require('cors')
const bodyParser = require('body-parser')

//2 - Instanciar express
const app = express()

//3- Add os complementos ao projeto
app.use(morgan('dev'))//morgan ao projeto para que tenhamos o log de execução
app.use(bodyParser.urlencoded({ extended: false}))
app.use(express.json()) //serve para informar o tipo de dados que queremos receber, que no nosso caso será um JSON
app.use(cors())// para definir quem pode comunicar coma  api

app.listen(8081, () => {
    console.log('Express iniciado em http://localhost:8081')
})