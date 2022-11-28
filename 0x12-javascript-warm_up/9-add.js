#!/usr/bin/node
const process = require('process');
const ac = parseInt(process.argv[2]);
const ac2 = parseInt(process.argv[3]);
function add (a, b) {
  console.log(a + b);
}
add(ac, ac2);
