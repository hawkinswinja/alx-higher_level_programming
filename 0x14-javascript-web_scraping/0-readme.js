#!/usr/bin/node
const fs = require('fs').promises;
// read contents of file passed as argument
async function read (file) {
  try {
    const data = await fs.readFile(file, 'UTF8');
    console.log(data.toString());
  } catch (error) {
    console.log(error);
  }
}

read(process.argv[2].toString());
