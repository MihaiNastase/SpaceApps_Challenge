from flask import Flask, render_template
from flask_socketio import SocketIO
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('onconnect')
def handle_message(data):
    #Return message log here to begin with
    socketio.emit('response', 'Connected successfully')


if __name__ == '__main__':
    socketio.run(app)