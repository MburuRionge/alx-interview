#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function[2], function (err, res, body) {
	(err) throw err;
	const filmakers = JSON.parse(body).characters;
	exactOrder(filmakers, 0);
});
const exactOrder = (filmakers, x) => {
	if (x == filmakers.length) return;
	request(filmakers[x], function (err, res, body) {
		if (err) throw err;
		console.log(JSON.parse(body).name);
		exactOrder(filmakers, x + 1);
	});
};
