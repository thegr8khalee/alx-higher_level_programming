#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const count = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      count++;
    }
  }
    return count;
}