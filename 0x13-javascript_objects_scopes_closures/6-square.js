#!/usr/bin/node
/* class Square that defines a square
and inherits from Square of 5-square.js */

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) console.log('C'.repeat(this.width));
    }
  }
};
