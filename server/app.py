from flask import Flask, jsonify
from flask_cors import CORS
from log_model import LogModel
from flask_bcrypt import Bcrypt
from db import db
from authService import authService


app = Flask(__name__)
CORS(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'nasa_lunar'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

dbConnection = db(app)
authService = authService(app)

authService.create_user('admin', 'admin')

@app.route('/', methods = ['GET'])
def get_logs():
    return jsonify({"Hello":"World!"})

@app.route('/test', methods =['GET'])
def get_test():
    return LogModel("user112", "Huston, we have a problem").toJson()

if __name__ == "__main__":
    app.run(debug=True)