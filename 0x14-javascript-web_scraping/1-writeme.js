#!/usr/bin/node
const fs = require('fs');
const path = process.argv[2];
const argm = process.argv[3];

fs.writeFile(path, argm, function (err) {
  if (err) {
    console.log(err);
  }
});
