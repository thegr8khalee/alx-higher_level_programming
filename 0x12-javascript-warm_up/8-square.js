#!/usr/bin/node
const n = Math.floor(Number(process.argv[2]));
for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
        console.log('X');
    }
    console.log('\n');
}
