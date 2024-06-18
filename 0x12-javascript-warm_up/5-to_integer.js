#!/usr/bin/node
const integer = Math.floor(Number(process.argv[2]));
console.log(isNaN(integer) ? 'Not a number' : `My number: ${integer}`);
