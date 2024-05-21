#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const write_ = process.argv[3];

fs.writeFile(file, write_, 'utf8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
});
