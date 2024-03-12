#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
      if ((w > 0) && (h > 0)) {
        this.width = w;
        this.height = h;
      }
    }
    print() {
        const size = Math.floor(Number(process.argv[2]));
        if (isNaN(size)) {
          console.log('Missing size');
        } else {
          for (let r = 0; r < height; r++) {
            let row = '';
            for (let c = 0; c < width; c++) row += 'X';
              console.log(row);
          }
        }
      }
  }
  
  module.exports = Rectangle;