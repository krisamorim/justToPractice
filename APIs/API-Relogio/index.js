const express = require('express')
const morgan = require('morgan')
const app = express()
const queries = require('./src/data/queries.json')
const clientPG = require('pg').Client
const connectDB = new clientPG({
    user: 'postgres',
    host: 'localhost',
    database: 'anglehours',
    password: '12345',
    port: 5432
})
app.use(morgan('dev'))


//função para encontrar o angulo
function findAngule(h,m){
    //concatenando hora e minuto para utilizar na query
    let desiredTime = `${h}:${m}`
    
    //busca no arquivo queries o objeto que tem o atributo time igual ao valor daa variavel desiredTime, se encontrar retorna o objeto com o angulo e o time, se não encontrar retorna false
    let querieFound = queries.find((querie) => {
        //compara se o valor de querie.time (é o valor do time de cada objeto de dentro do arquivo queries) com o valor da variavel desireTime
        return querie.time === desiredTime;
    })

    //se encontrou retorne o atributo angulo do objeto encontrado 
    if(querieFound){
        return querieFound['angle']
    }else{ //se não foi encontrado pegue no db e coloque no json
        let resu = getAngle()
        async function getAngle(){
            try{
            console.log('conectando ao DB postgre..')
            await connectDB.connect()
            console.log('Conexão bem sucedida')

            let queryGetAngle = 'select angle from tabledefault where hour = ' + h + ' AND minute = ' + m
            console.log(queryGetAngle)

            let resultado = await (await connectDB.query(queryGetAngle)).rows

            console.log(resultado)
            }

            finally{
                await connectDB.end()
                console.log("Desconectado")
            }
        
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
}

//rota defaul para ler o json
app.get('/', (req, res) => {
    return res.json(queries)
})

//rota p pegar hora e minuto
app.get('/clock/:hour/:minutes?', (req, res) => {
    let hour = req.params.hour
    let minutes = req.params.minutes

    //if para definir minutes como 0 caso não seja informado
    if(minutes === undefined){
        minutes = 0
    }
    //passa a hora e minuto para a função findAngule
    return res.json(findAngule(hour,minutes))
})

app.listen(8080, () => {
    console.log('Server iniciado na porta 8080')
})