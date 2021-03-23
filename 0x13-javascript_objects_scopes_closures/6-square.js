#!/usr/bin/node
const Square1 = require('./5-square.js');
module.exports = class Square extends Square1 {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        if (!c || c.length !== 1) {
          str += 'X';
        } else {
          str += c;
        }
      }
      console.log(str);
    }
  }
};
