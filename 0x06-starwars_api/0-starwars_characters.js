#!/usr/bin/node

const request = require("request");
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    getCharacterName(characters, 0);
  }
});

function getCharacterName(characters, index) {
  if (index === characters.length) return;
  const characterPath = characters[index];
  request(characterPath, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      getCharacterName(characters, index + 1);
    }
  });
}
