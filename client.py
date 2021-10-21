import pandas as pd
import socketio
import json
import os

sio = socketio.Client()

message = {
    'image': 'https://z3.ax1x.com/2021/09/26/46iYlR.png',
    'lang': 'ch'
}
message = json.dumps(message)
sio.connect('http://127.0.0.1:5000/')
num = 0


@sio.on('message')
def handle_message(msg):
    global num
    if msg[:6] == f"表格坐标为:":
        num += 1
        msg = f"表格{num}坐标为:\n" + message[7:]

    if msg[3:5] == f'内容':
        msg = msg[8:]
        df_json = pd.read_json(msg)
        msg = f"表格{num}内容为：\n" + str(df_json)
        if not os.path.exists("./results/table/"):
            os.makedirs("./results/table/")
        df_json.to_excel(f"./results/table/table_{num}.xlsx")
    print(msg)


@sio.on('disconnected')
def disconnect():
    sio.disconnect()


sio.emit('json', message)
