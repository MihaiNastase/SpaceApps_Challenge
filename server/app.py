from flask import Flask, jsonify, render_template, redirect, url_for, request, flash, session
from flask_cors import CORS
from db import db
from authService import authService
from flask_marshmallow import Marshmallow
from flask.wrappers import Response
from flaskext.mysql import MySQL
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_socketio import SocketIO
from websocket import websocket

app = Flask(__name__)
CORS(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#####################################################################
app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'nasa_lunar'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

login_manager = LoginManager()
login_manager.init_app(app)

socketio = SocketIO(app)

dbConnection = db(app)
authService = authService(app)
websocket = websocket(app)

authService.create_user('admin', 'admin')
authService.create_user('paul', 'paul')
authService.select_user('admin')
#loginResp = authService.login('admin', 'admin')
#if(loginResp != False):
#    login_user(loginResp)
dbConnection.add_logs()
#####################################################################

@socketio.on('onconnect')
#@login_required
def handle_message():
    #Return message log here to begin with
    socketio.emit('inital_log', websocket.get_logs())

@socketio.on('send_message')
def send_message(data):
    socketio.emit('update_log', websocket.get_specific_log(websocket.log_message(data['userId'], data['message_text'], data['verified'])))

@app.route('/log', methods = ['GET'])
def websocket_test():
    return render_template('websocket.html')

@app.route('/', methods = ['GET'])
def home():
    return jsonify({"Hello":"World!"})

@app.route('/logs', methods = ['GET'])
def get_logs():
    data = dbConnection.get_logs()
    return jsonify(data)

@app.route('/logs', methods = ['POST'])
def post_log():
    log = request.get_json()
    return jsonify(log)
    
@app.route('/test', methods =['GET'])
def get_test():
    return LogModel("user112", "Huston, we have a problem").toJson()

@app.route('/logout')
@login_required
def logout():
    logout_user()
    
@app.route('/profile')
@login_required
def profile():
    return "Logged in - profile"



@app.route('/login', methods=['POST'])
def login_post():
    creds = request.get_json()
    #print(creds)
    username = creds['username'] #request.form.get('username')
    password = creds['password'] #request.form.get('password')

    loginResp = authService.login(username, password)
    if(loginResp != False):
        login_user(loginResp)
        return ({"status": True, "message": "Successfully logged in!"})
    else:
        return ({"status": False, "message": "Failed to log in, please check your login combination again"})

@app.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('username')
    password = request.form.get('password')

    loginResp = authService.select_user(username)
    if(loginResp == False):
        authService.create_user(username, password)
        return "Success"
    else:
        return "Failure"

@login_manager.user_loader
def load_user(user_id):
    resp = authService.get_user_by_id(user_id)
    if(resp != False):
        return resp
    return None

if __name__ == "__main__":
    app.run(debug=True)