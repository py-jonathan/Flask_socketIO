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
  - Recieve messages with JSON format from the client.
  - Run the model with received messages.
  - Send messages to the client.
- **client.py**
  - *EmbeddingNet* - base network for encoding images into embedding vector
  - *ClassificationNet* - wrapper for an embedding network, adds a fully connected layer and log softmax for classification
  - *SiameseNet* - wrapper for an embedding network, processes pairs of inputs
  - *TripletNet* - wrapper for an embedding network, processes triplets of inputs
