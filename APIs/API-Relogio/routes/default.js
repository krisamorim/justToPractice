const express = require('express');
const router = express.Router();
const queries = require('../src/data/queries.json');

//rota default para ler o json
router.get('/', (req, res,) => {
    return res.json(queries)
});

router.post('/', (req, res) => {
    res.status(200).send('Usando POST')
});

module.exports = router