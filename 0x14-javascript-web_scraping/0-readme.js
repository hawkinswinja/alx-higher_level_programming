#!/usr/bin/node
const fs = require('fs').promises;
// read contents of file passed as argument
async function read (file) {
  try {
    const data = await fs.readFile(file);
    console.log(data.toString());
  } catch (error) {
    console.error(error);
  }
}

read(process.argv[2].toString());
