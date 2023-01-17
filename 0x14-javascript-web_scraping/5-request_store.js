#!/usr/bin/node
const request = require('request');
const fs = require('fs').promises;
// write the body to file
request.get(process.argv[2], function (error, response, body) {
  if (error) { console.log(error); }
  if (body) {
    fs.writeFile(process.argv[3], body, 'UTF8');
  }
});
