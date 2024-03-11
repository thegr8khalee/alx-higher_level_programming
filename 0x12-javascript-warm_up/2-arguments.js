#!/usr/bin/node
const arg = process.argv.slice(2);
const args = arg.length;
if (args === null) {
    console.log('no argument');
} else if (args === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
