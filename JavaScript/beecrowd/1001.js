let input = require('fs').readFileSync('./stdin', 'utf8');
let lines = input.split('\n');
// var,let,const -> let ou const
let n1 = parseInt(lines[0])
let n2 = parseInt(lines[1])
// string -> '' e "", ``
console.log(`X = ${n1+n2}`)
