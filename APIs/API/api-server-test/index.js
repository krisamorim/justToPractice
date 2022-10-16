const express = require('express')

const server = express()

server.use(express.json())

const leads = [
    {   "idLead": 11,
        "empresa": "Empresa 01",
        "createAt": new Date(),
        "contatos":
            { 
                "idLead": 11,
                "idContact": 1111,
                "name": "Fernando Melo",
                "email": "developer@email.com",
                "phone": "4199999999"
            },
        "timeline": "Descrição"
    },
    {   "idLead": 22,
        "empresa": "Empresa 01",
        "createAt": new Date(),
        "contatos":
            { 
                "idLead": 22,
                "idContact": 3333,
                "name": "Fernando Melo",
                "email": "developer@email.com",
                "phone": "4199999999"
            },
        "timeline": "Descrição"
    },
]

//LIST LEADS
server.get('/leads', (req, res) =>{
    return res.json(leads)
})

//CREATE LEADS
server.post('/leads', (req, res) => {
    const body = {
        id: req.body.idLead,
        empresa: req.body.empresa,
        createAt: req.body.createAt,
        contatos: req.body.contatos,
        timeline: req.body.timeline
    }

    leads.push(body)

    return res.json(leads)
})

//EDIT LEADS
server.put('/leads/:index', (req, res) => {
    const { index } = req.params
    
    const body = {
        id: req.body.idLead,
        empresa: req.body.empresa,
        createAt: req.body.createAt,
        contatos: req.body.contatos,
        timeline: req.body.timeline
    }

    leads[index] = body

    return res.json(leads)
})

//DELETE LEADS
server.delete('/leads/:index', (req, res) => {
    const { index } = req.params;

    leads.splice(index, 1);
    
    return res.json(leads)
})

server.listen(3000)