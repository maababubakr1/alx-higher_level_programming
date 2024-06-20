#!/usr/bin/node
// prints two arguments passed to it, in the following format: “ is ”

const integer = Math.floor(Number(process.argv[2]));
console.log(isNaN(integer) ? 'Not a number' : `My number: ${integer}`);
