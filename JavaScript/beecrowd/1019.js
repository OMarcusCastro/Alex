var input = require('fs').readFileSync('./stdin', 'utf8');
var lines = input.split('\n');

let n = parseInt(lines[0])
// a = q*d + r -> a-r/d = q
let horas = (n - n%(60*60))/(60*60)
n = n % (60*60)

let minutos = (n - n%(60))/(60)
n = n % 60

console.log(`${horas}:${minutos}:${n}`)