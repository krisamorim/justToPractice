const express = require('express')
const routes = express.Router()

// passos 5 , 6 e 7 movidos para ca no passo 10

//5- simulando DB
let db = [
    { '1': { Nome: 'Cliente 1', idade: '20'}},
    { '2': { Nome: 'Cliente 2', idade: '30'}},
    { '3': { Nome: 'Cliente 3', idade: '40'}}
]

//6- sem caminho especifico, sendo somente a rota raiz como caminho do get
//11- alterar app.get para routes.get
routes.get('/', (req, res) => {
    return res.json(db)
})

//7- update
//12- alterar app.post para routes.post
routes.post('/add', (req, res) => {
    const body = req.body

    if(!body)
        return res.status(400).end()
        
    
    db.push(body)
    return res.json(body)
})


//13- adicionando o delete
routes.delete('/:id', (req, res) => {
    const id = req.params.id

    //14- Filtar a variavel DB sem o item especificado para simular a exclusão
    let newDB = db.filter(item => {
        if(!item[id])
            return item
    })

    //atualizar banco
    db = newDB;
    return res.send(newDB)
})

module.exports = routes