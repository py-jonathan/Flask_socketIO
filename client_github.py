import socketio
import json

sio = socketio.Client()

message = {
    'image': 'https://z3.ax1x.com/2021/09/26/46iYlR.png',
    'lang': 'ch'
}
message = json.dumps(message)
sio.connect('http://127.0.0.1:5000/')


@sio.on('message')
def handle_message(msg):
    print(f"{msg}")


@sio.on('disconnected')
def disconnect():
    sio.disconnect()


sio.emit('json', message)
