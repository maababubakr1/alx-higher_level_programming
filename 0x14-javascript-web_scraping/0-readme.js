#!/usr/bin/node
const fs = require('fs');
const argm = process.argv[2];

fs.readFile(argm, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
