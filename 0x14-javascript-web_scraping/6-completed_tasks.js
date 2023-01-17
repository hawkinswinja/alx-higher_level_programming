#!/usr/bin/node
const request = require('request');
// get number of completed task for each user
request(process.argv[2], function (error, response, body) {
  if (error) { console.log(error); }
  if (body) {
    const alltasks = JSON.parse(body);
    const completed = alltasks.filter(function (task) {
      return task.completed === true;
    });
    const usertasks = {};
    for (let userid = 1; userid <= 10; userid++) {
      const mytasks = completed.filter(function (task) {
        return task.userId === userid;
      });
	  if (mytasks.length > 0) { usertasks[userid.toString()] = mytasks.length; }
    }
    console.log(usertasks);
  }
});
