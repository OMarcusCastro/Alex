var input = require('fs').readFileSync('./stdin', 'utf8');
var lines = input.split('\n');

let r = parseFloat(lines[0])
const pi = 3.14159
let area = pi*r**2

console.log(`A = ${area.toFixed(4)}`)