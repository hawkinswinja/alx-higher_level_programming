#!/usr/bin/node
const process = require('process');
const ac = process.argv.length - 2;
if (ac < 1) {
  console.log('No argument');
} else if (ac === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
