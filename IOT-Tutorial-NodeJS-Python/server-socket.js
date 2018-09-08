module.paths.push('/usr/local/lib/node_modules');
var port = 5000;
var app = require('express')();
var http = require('http');
var server = http.Server(app);
server.listen(port, '0.0.0.0');
var io = require('socket.io').listen(server);

var iot = io.of('/iot');
iot.on('connection', function(socket){
  socket.on('led', function(msg){
    console.log(msg);
    socket.broadcast.emit('led', msg);
  });
});

console.log('Express server listening on port ' + port);
