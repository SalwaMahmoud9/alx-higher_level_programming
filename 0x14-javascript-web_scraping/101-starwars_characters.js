#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    const l = [];
    characters.forEach(ch => {
      l.push(new Promise((resolve, reject) => {
        request.get(ch, function (err, res, body) {
          if (err) {
            reject(err);
          } else if (res.statusCode === 200) {
            resolve(JSON.parse(body).name);
          }
        });
      }));
    });
    Promise.all(l).then(names => {
      names.forEach(name => console.log(name));
    });
  }
});
