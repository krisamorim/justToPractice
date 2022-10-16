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

// o passo 5, 6 e 7 foram movidos para o arquivo routes no passo 10


//4- startando server
app.listen(8081, () => {
    console.log('Server startado na porta 8081')
})