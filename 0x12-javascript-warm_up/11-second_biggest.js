#!/usr/bin/node
const process = require('process');
const argv = process.argv;
const ac = argv.length - 2;
if (ac <= 1) {
  console.log(0);
} else {
  let max = 0;
  for (let x = 2; x < argv.length; x++) {
    if (parseInt(argv[x]) > max) {
      max = argv[x];
    }
  }
  let diff = max;
  let min = max;
  for (let n = 2; n < argv.length; n++) {
    diff = max - argv[n];
    if (diff < min && diff !== 0) {
      min = diff;
    }
  }
  console.log(max - min);
}
