#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) { console.log(error); }
  if (response.statusCode === 200) {
    const movies = JSON.parse(body).results;
    let appeared = 0;
    for (const movie of movies) {
      for (const charURL of movie.characters) {
        if (charURL.includes(18)) { appeared++; }
      }
    }
    console.log(appeared);
  }
});
