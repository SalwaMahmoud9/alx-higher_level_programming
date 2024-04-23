#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    const arr = [];
    characters.forEach(ch => {
      arr.push(new Promise((resolve, reject) => {
        request.get(ch, function (error, response, body) {
          if (!error) {
            resolve(JSON.parse(body).name);
          } else if (error) {
            reject(error);
          }
        });
      }));
    });
    Promise.all(arr).then(names => {
      names.forEach(name => console.log(name));
    });
  }
});
