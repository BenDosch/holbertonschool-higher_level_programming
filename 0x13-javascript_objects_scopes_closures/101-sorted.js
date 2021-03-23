#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const key in dict) {
  if (!(dict[key] in newDict)) {
    newDict[dict[key]] = [];
  }
  const list = newDict[dict[key]];
  list.push(key);
}
console.log(newDict);
