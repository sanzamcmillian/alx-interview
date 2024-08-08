#!/usr/bin/node

const request = require('request');

request('https://swapi-api.alx-tools.com' + process.argv[2], function (error, response, body) {
  if (error) throw error;
  const actors = JSON.parse(body).characters;
  exactOrder(actors, 0);
});
const exactOrder = (actors, x) => {
  if (actors.length === x) return;
  request(actors[x], function (error, response, body) {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    exactOrder(actors, x + 1);
  });
};
