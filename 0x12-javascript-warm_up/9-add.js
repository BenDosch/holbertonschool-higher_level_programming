#!/usr/bin/node
function add(a, b) {
  a = parseInt(a);
  b = parseInt(b);
  if (a && b) {
    return (a + b);
  } else {
    return NaN;
  }
};
console.log(add((process.argv[2]), process.argv[3]));
