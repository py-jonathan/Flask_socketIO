# Flask_Socketio_API
Flask_SoketIO implementation of an algorithmn API. The API is based on the websocket and can asynchronously return data to clients.


# Installation
+ python3.7
+ flask_socketio
+ flask
+ websocket-client
+ python-socketio
+ python-engineio
+ python-dateutil
+ requests

You can also install packages with pip install
```pyhon
pip install -r requirements
```

# Code Structure
- **server.py**
  - Recieve messages with JSON format from the client
  - Run the model with received messages
  - Send messages to the client <br />
- **client.py**
  - Send messages with JSON format to the server
  - Recieve results from the server

