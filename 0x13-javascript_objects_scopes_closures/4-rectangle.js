#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
      if ((w > 0) && (h > 0)) {
        this.width = w;
        this.height = h;
      }
    }

    print () {
        const size = Math.floor(Number(process.argv[2]));
        if (!this.width || !this.height) {
            return;
        } else {
          for (let r = 0; r < this.height; r++) {
            let row = '';
            for (let c = 0; c < this.width; c++) row += 'X';
              console.log(row);
          }
        }
    }

    double () {
        if (!this.width || !this.height) {
          return;
        } else {
          this.height = this.height * 2;
          this.width = this.width * 2;
        }
    }

    rotate () {
        if (!this.width || !this.height) {
            return;
        } else {
            const temph = this.height;
            const tempw = this.width;
            this.height = tempw;
            this.width = temph;
        }
    }
}
module.exports = Rectangle;
