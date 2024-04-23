#!/usr/bin/node
const request = require('request');
const dict1 = {};

request(process.argv[2], function (error, data, body) {
  if (!error) {
    const todos = JSON.parse(body);

    for (let i = 0; i < todos.length; i++) {
      if (todos[i].completed === true) {
        if (dict1[todos[i].userId] === undefined) {
          dict1[todos[i].userId] = 1;
        } else {
          dict1[todos[i].userId] += 1;
        }
      }
    }
  }
  console.log(dict1);
});
