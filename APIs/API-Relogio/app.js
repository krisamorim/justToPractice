const express = require('express');
const app = express();
const morgan = require('morgan'); //é utilizado par amostrar logs

//rotas
const rotaDefault = require('./routes/default');
const rotaClock = require('./routes/clock');

app.use(morgan('dev'));//carregar para mostrar as requisições no terminal
app.use('/', rotaDefault);
app.use('/clock', rotaClock)

//quando não encontrar rota
app.use((req, res, next) =>{
    const erro = new Error('Endereço não encontrado');
    erro.status = 404;
    next(erro);
});
//quando não encontrar rota (necessário p/ o codigo acima)
app.use((error, req, res, next) => {
    res.status(error.status || 500)
    return res.send({
        erro: {
            mensagem: error.message
        }
    })
})

module.exports = app;