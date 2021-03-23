#!/usr/bin/node
const ary = process.argv;
ary.shift();
ary.shift();
let max = ary[1];
let second = max;
if (ary[1]) {
  ary.forEach(function (item) {
    const num = parseInt(item);
    if (num > second && num > max) {
      second = max;
      max = num;
    } else if (num > second) {
      second = num;
    }
  });
  console.log(second);
} else {
  console.log(0);
}
