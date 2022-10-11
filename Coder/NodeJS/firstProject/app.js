const fs = require("fs");
let moment = require('moment');

let superHerois = require('./superHerois')

let dados = fs.readFileSync(__dirname + '/dados.txt', 'utf8')
let data = moment().format('MMM dd YYYY')

console.log(superHerois);
console.log(dados);