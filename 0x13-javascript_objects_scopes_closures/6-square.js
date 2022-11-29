#!/usr/bin/node
const a = require('./5-square.js');

module.exports = class Square extends a {
  charPrint (c) {
    if (c) {
      let chars = '';
      for (let w = 0; w < this.width; w++) {
        chars += c;
      }
      for (let h = 0; h < this.height; h++) {
        console.log(chars);
      }
    } else {
      this.print();
    }
  }
};
