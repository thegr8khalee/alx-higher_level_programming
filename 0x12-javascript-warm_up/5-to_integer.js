#!/user/bin/node
const n = Math.floor(Number(process.argv[2]));
console.log(isNaN(n) ? 'Not a number' : 'my number: ' + n);