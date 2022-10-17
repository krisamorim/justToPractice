const express = require('express')
const app = express()
const clientPG = require('pg').Client
const connectDB = new clientPG({
    user: 'postgres',
    host: 'localhost',
    database: 'anglehours',
    password: '12345',
    port: 5432
})

app.get('/vinl/rest/clock/:hour', (req, res) => {
    let hour = req.params.hour
    let minutes = "0"

    let resu = getAngle()

    async function getAngle(){
        try{
        console.log('conectando ao DB postgre..')
        await connectDB.connect()
        console.log('Conexão bem sucedida')

        let queryGetAngle = 'select angle from tabledefault where hour = ' + hour + 'AND minute = ' + minutes
        let resultado = await (await connectDB.query(queryGetAngle)).rows

        console.log(resultado)
        }

        finally{
            await connectDB.end()
            console.log("Desconectado")
        }
    }
    return res.json(resu)
})

app.listen(8080, () => {
    console.log('Server iniciado na porta 8080')
})
