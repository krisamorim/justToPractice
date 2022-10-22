const express = require('express');
const router = express.Router();
const queries = require('../src/data/queries.json')

const clientPG = require('pg').Client
const connectDB = new clientPG({
    user: 'postgres',
    host: 'localhost',
    database: 'anglehours',
    password: '12345',
    port: 5432
})

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
        async function getAngle(){
            try{
                console.log('conectando ao DB postgre..')
                await connectDB.connect()
                console.log('Conexão bem sucedida')
                //montando query
                let queryGetAngle = 'select angle from tabledefault where hour = ' + h + ' AND minute = ' + m

                //consultar no banco
                return await (await connectDB.query(queryGetAngle)).rows
            }

            finally{
                await connectDB.end()
                console.log("Desconectado")
            }

            return resultado
        }

        let resu = getAngle()

        console.log(resu)
        if(resu == 0){
            console.log('calcular')
            console.log('add ao db')
        }

    }
}

//rota p pegar hora e minuto
router.get('/:hour/:minutes?', (req, res) => {
    let hour = req.params.hour
    let minutes = req.params.minutes

    //if para definir minutes como 0 caso não seja informado
    if(minutes === undefined){
        minutes = 0
    }
    //passa a hora e minuto para a função findAngule
    return res.json(findAngule(hour,minutes))
    //res.status(200).send(`hour: ${hour} and minute ${minutes}`)
})

module.exports = router;