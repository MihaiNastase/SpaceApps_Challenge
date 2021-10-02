from flask import Flask
from flaskext.mysql import MySQL
from db import db

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'nasa_lunar'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

dbConnection = db(app)

@app.route('/')
def hello():
    return 'Hello, World!'