import numpy as np
import serial
import json
from socketIO_client_nexus import SocketIO, BaseNamespace

ser = serial.Serial('/dev/ttyUSB0')
# replace with correct ip or address and port
socketIO = SocketIO('X.X.X.X', 9999)
directory_namespace = socketIO.define(BaseNamespace, '/directory')

while True:
    try:
        data = str(ser.readline()[:-2]).split(',')
        directory_namespace.emit('backend',json.dumps({'from':'backend', 'data': }))
    except:
        pass
        # dont do sleep in python, do sleep using arduino
        # because why, python only a transmitter, serial port only listen, cannot send something to our devices
