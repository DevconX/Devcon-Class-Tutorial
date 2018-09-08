module.paths.push('/usr/local/lib/node_modules');
var port = 5000;
var app = require('express')();
var http = require('http');
var server = http.Server(app);
server.listen(port, '0.0.0.0');
var mysql = require('mysql');
var io = require('socket.io').listen(server);

var consensor = mysql.createConnection({
  host: "ec2-13-229-88-110.ap-southeast-1.compute.amazonaws.com",
  user: "husein",
  password: "husein",
  database: "sensor"
});

var iot = io.of('/iot');
iot.on('connection', function(socket){
  socket.on('led', function(msg){
    socket.broadcast.emit('led', msg);
  });
  socket.on('dht11', function(msg){
    var temp = JSON.parse(msg);
    consensor.query("INSERT INTO sensor(humidity, temperature) VALUES ("+parseInt(temp['humidity'])+","+parseInt(temp['temperature'])+")", function (err, result) {
      if (err) throw err;
      console.log('inserted into mysql');
    });
    socket.broadcast.emit('dht11', msg);
  });
});

console.log('Express server listening on port ' + port);
