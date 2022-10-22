const express = require('express');
const app = express();

//rotas
const rotaDefault = require('./routes/default');
const rotaClock = require('./routes/clock');

app.use('/', rotaDefault);
app.use('/clock', rotaClock)


module.exports = app;