#!/usr/bin/node

const argument = parseInt(process.argv[2]);
if (argument) {
  console.log('My number: ' + argument);
} else {
  console.log('Not a number');
}
