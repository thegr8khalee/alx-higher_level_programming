#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor(size) {
    const len = process.argv.length;
    if (len > 2) {
      return;
    } else {
      super(size, size);
    }
  }
}
module.exports = Square;
