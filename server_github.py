from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import os
import requests
import json
import socketio
import shutil
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode="threading")


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


@socketio.on('message')
def handle_message(message):
    print('received message' + message)


@socketio.on("json")
def handle_json(json_file):
    img_name = None
    try:
        json_file = json.loads(json_file)
        print('recevied json: ' + str(json_file))
        lang = json_file["lang"]
        send("接收成功， 正在运行模型......")
        img_name = download_img(json_file["image"])
        res = run_model(img_name, lang)
        send(res)
        emit("disconnected")
    except Exception as e:
        send(f"请求出错, {e}")
        emit("disconnected")

    if img_name is not None:
        os.remove(img_name)
        shutil.rmtree(f"./output/table/{img_name.split('/')[-1][:-4]}")


def run_model(img_name, lang):
    time.sleep(15)
    res = f"img_name: {img_name}, lang: {lang}"
    return res


def generate_img_name(url):
    img_name = url.split('/')[-1]
    return img_name


def download_img(url):
    img_name = generate_img_name(url)
    response = requests.get(url)
    file = open(img_name, "wb")
    file.write(response.content)
    file.close()
    return img_name


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0")

