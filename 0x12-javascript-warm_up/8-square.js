#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (size) {
  for (let a = 0; a < size; ++a) {
    let b = 0;

    for (; b < size; ++b) {
      process.stdout.write('X');
    }

    if (b === size) {
      console.log('');
    }
  }
} else {
  console.log('Missing size');
}
