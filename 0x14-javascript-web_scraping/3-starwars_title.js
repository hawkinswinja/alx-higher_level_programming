#!/usr/bin/node
const request = require('request');
// returns the status code of a URL
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2].toString();
request(url, function (error, response, body) {
  if (error) { console.error(error); }
  if (response.statusCode ===200 && body) {
    console.log(JSON.parse(body).title);
  }
});
