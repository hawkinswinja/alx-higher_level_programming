#!/usr/bin/node
const process = require('process');
const ac = parseInt(process.argv[2]);
function fact (a) {
  if (a === 0 || isNaN(a)) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}
console.log(fact(ac));
