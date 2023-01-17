#!/usr/bin/node
const request = require('request');
const fs = require('fs');
// write the body to file
request.get(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
