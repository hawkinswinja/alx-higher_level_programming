#!/usr/bin/node
exports.esrever = function (list) {
  let n = list.length - 1;
  let i = 0;
  const list2 = [];
  while (n >= 0) {
    list2[i] = list[n];
    i++;
    n--;
  }
  return list2;
};
