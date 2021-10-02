from flask import Flask
from flaskext.mysql import MySQL
from flask_bcrypt import Bcrypt
from db import db
from authService import authService

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'nasa_lunar'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

dbConnection = db(app)
authService = authService(app)

authService.create_log(12, 'test', 0)

authService.create_user('admin', 'admin')
@app.route('/')
def hello():
    return 'Hello, World!'
