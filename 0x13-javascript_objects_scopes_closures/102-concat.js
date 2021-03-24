#!/usr/bin/node
const fs = require('fs');
const src1 = process.argv[2];
const src2 = process.argv[3];
const dest = process.argv[4];
const a = fs.readFileSync(src1, { encoding: 'utf8', flag: 'r' },
  function (err) {
    if (err) {
      return console.error(err);
    }
  });
const b = fs.readFileSync(src2, { encoding: 'utf8', flag: 'r' },
  function (err) {
    if (err) {
      return console.error(err);
    }
  });
fs.writeFile(dest, a, function (err) {
  if (err) {
    return console.error(err);
  }
});
fs.appendFile(dest, '\n' + b, function (err) {
  if (err) {
    return console.error(err);
  }
});
