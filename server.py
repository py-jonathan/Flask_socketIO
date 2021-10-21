from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import requests
import json
import socketio
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
    try:
        json_file = json.loads(json_file)
        print('recevied json: ' + str(json_file))
        lang = json_file["lang"]
        send("Successfully received, the model is running...")
        img_name = download_img(json_file["image"])
        res = run_model(img_name, lang)
        send(res)
        emit("disconnected")
    except Exception as e:
        send(f"Request error, {e}")
        emit("disconnected")


def run_model(img_name, lang):
    time.sleep(10)
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

