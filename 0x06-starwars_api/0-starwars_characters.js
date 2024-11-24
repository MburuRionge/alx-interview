#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
if (!filmId) {
	console.error('Usage: ./0-starwars_characters.js <film_id>');
	process.exit(1);
}

// fwtch fim details by id
request(`https://swapi-api.hbtn.io/api/films/${filmId}`, (err, res, body) => {
	if (err) {
		console.error(err);
		process.exit(1);
	}

	try {
		const characters = JSON.parse(body).characters;
		fetchCharacters(characters, 0);
	} catch (error) {
		console.error('Error parsing JSON:', error);
		process.exit(1);
	}
});

//recursive function to fetch characters in order
const fetchCharacters[index], (err, res, body) => {
	if (err) {
		console.error{err};
		return;
	}

	try {
		const name = JSON.parse(body).name;
		console.log(name);
	} catch (error) {
		console.error(characters, index _ 1);
	});
};
