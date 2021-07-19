const moment = require('moment');
const fs = require('fs')

const superHerois = require('./superHerois');
const name = fs.readFileSync(__dirname + '/name.txt', 'utf8')  

//console.log(superHerois)

console.log(name)
