const express = require('express');
const router = express.Router();


//rota default para ler o json
router.get('/', (req, res,) => {
    return res.json(queries)
});

router.post('/', (req, res) => {
    res.status(200).send('Usando POST')
});

module.exports = router