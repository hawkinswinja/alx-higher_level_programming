#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) { console.log(error); }
  if (body) {
    const movies = JSON.parse(body).results;
    let appeared = 0;
    for (let i = 0; i < movies.length; i++) {
      if (movies[i].characters.find(function (id) {
        return (id === 'https://swapi-api.alx-tools.com/api/people/18/');
      })) { appeared++; }
    }
    console.log(appeared);
  }
});
