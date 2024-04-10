#!/usr/bin/node

const args = parseInt(process.argv[2]);

if (args) {
  for (let a = 0; a < args; ++a) {
    console.log('C is fun');
	}
} else {
  console.log('Missing number of occurrences');
}
