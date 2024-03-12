#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0) {
      this.width = 0;
      this.height = 0;
    } else {
        this.width = w;
        this.height = h;
    }
  }
}

modules.exports = Rectangle;