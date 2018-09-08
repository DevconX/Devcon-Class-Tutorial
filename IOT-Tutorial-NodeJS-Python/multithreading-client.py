from socketIO_client_nexus import SocketIO, BaseNamespace
import json
from threading import Thread
import threading

socketIO = SocketIO('ip', port)
namespace = socketIO.define(BaseNamespace, '/directory')

def receive_events_thread():
    socketIO.wait()
def on_response(*args):
    global emotion_batch
    loads = json.loads(args[0])
    try:
        for i in loads['database']:
            emotion_batch.append(dict_emotion[i['emotion']])
    except Exception as e:
        pass

socketIO = SocketIO('ip', port)
namespace = socketIO.define(BaseNamespace, '/directory')
namespace.on('update', on_response)
receive_events_thread = Thread(target=receive_events_thread)
receive_events_thread.daemon = True
receive_events_thread.start()

while True:
    # do something while listen to socket
