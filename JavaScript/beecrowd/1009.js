var input = require('fs').readFileSync('./stdin', 'utf8');
var lines = input.split('\n');

let nome = lines[0]
let salario = parseFloat(lines[1])
let venda = parseFloat(lines[2])

let bonus = venda*0.15
let total = bonus+salario

console.log(`TOTAL = R$ ${total.toFixed(2)}`)