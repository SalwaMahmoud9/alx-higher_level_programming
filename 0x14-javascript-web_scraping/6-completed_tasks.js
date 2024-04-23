#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    let completed = {};
    
  
    for (let i = 0; i < todos.length; i++) {
      if (todos[i].completed === true) {
        if (completed[todos[i].userId] === undefined) {
          completed[todos[i].userId] = 1;
        } else {
          completed[ztodos[i].userId] += 1;
        }
      }
    }
  
    console.log(completed);
  }
});
