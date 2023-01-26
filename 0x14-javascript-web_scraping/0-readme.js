#!/usr/bin/node
const fs = require('fs');
// read contents of file passed as argument
fs.readFile(process.argv[2], 'utf-8', (error, data) => {
  if (error) { console.log(error); } else { console.log(data); }
});
