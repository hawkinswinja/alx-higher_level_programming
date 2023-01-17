#!/usr/bin/node
const fs = require('fs').promises;
// write contents to file passed as argument
async function writetofile (file, data) {
  try {
    await fs.writeFile(file, data);
  } catch (error) {
    console.error(error);
  }
}

writetofile(process.argv[2], process.argv[3]);
