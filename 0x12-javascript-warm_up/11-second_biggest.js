#!/usr/bin/node
const process = require('process');
const ac = process.argv.length - 2;
if (ac <= 1) {
  console.log(0);
} else {
  let max = 0;
  for (let x = 2; x < process.argv.length; x++) {
    if (parseInt(process.argv[x]) > max) {
      max = process.argv[x];
    }
  }
  console.log(max);
}
