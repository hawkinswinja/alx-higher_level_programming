#!/usr/bin/node
const process = require('process');
const args = parseInt(process.argv[2]);
if (isNaN(args)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < args; x++) {
    let arr = '';
    for (let i = 0; i < args; i++) {
      arr += 'x';
    }
    console.log(arr);
  }
}
