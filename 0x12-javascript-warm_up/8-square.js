#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (Number.isNaN(size)) {
	console.log('Missing size');
}else {
	console.log(size * 2);
}
