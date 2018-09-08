module.paths.push('/usr/local/lib/node_modules');
var io_client = require('socket.io-client');
var socket = io_client.connect('http://ec2-13-229-88-110.ap-southeast-1.compute.amazonaws.com:5000/iot', {reconnect: true});
var SerialPort = require('serialport');
var Readline = SerialPort.parsers.Readline;
var port = new SerialPort('/dev/ttyACM0');
var parser = new Readline();
port.pipe(parser);
parser.on('data', function(input){
  var input = input.split(':');
  socket.emit('dht11', JSON.stringify({'temperature':input[0], 'humidity':input[1].slice(0, -1)}));
});
