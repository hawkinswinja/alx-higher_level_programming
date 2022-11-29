exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  function count (item) {
    if (item === searchElement) {
      n++;
    }
  }
  list.forEach(count);
  return n;
};
