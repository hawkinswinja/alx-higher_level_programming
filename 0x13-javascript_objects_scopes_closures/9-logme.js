#!/usr/bin/node
let num = 0;
exports.logMe = function (item) {
  const disp = num + ': ' + item;
  console.log(disp);
  num++;
};
