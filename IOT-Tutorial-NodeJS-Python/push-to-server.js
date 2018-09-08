module.paths.push('/usr/local/lib/node_modules');
var io_client = require('socket.io-client');
var socket = io_client.connect('http://ec2-13-229-88-110.ap-southeast-1.compute.amazonaws.com:5000/iot', {reconnect: true});
var val = 0;
setInterval(function() {
  // we should replace with real sensor values
  socket.emit('led', JSON.stringify({'led': 'OK', 'val':val}));
  if(val == 0) val = 1;
  else val = 0;
}, 2000);
