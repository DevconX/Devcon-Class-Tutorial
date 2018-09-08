module.paths.push('/usr/local/lib/node_modules');
var io_client = require('socket.io-client');
var Gpio = require('onoff').Gpio;
var LED = new Gpio(22, 'out');
var socket = io_client.connect('http://ec2-13-229-88-110.ap-southeast-1.compute.amazonaws.com:5000/iot', {reconnect: true});
console.log('connected');
socket.on('led', function(msg){
  val = JSON.parse(msg);
  if(val['led']){
    LED.writeSync(val['val']);
  }
});
