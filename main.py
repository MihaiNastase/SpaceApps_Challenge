from flask import Flask, render_template, redirect, url_for, request, flash
from flask.wrappers import Response
from flaskext.mysql import MySQL
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask import session
from flask_login import login_user, logout_user, login_required
from db import db
from authService import authService

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'nasa_lunar'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

login_manager = LoginManager()
login_manager.init_app(app)

dbConnection = db(app)
authService = authService(app)

authService.create_user('admin', 'admin')
authService.select_user('admin')
#loginResp = authService.login('admin', 'admin')
#if(loginResp != False):
#    login_user(loginResp)
@app.route('/')
def hello():
    return 'Hello, World!'

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
    username = request.form.get('username')
    password = request.form.get('password')

    loginResp = authService.login(username, password)
    if(loginResp != False):
        login_user(loginResp)
        return ("Logged in")
    else:
        return "Login failed"

@app.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('username')
    password = request.form.get('password')

    loginResp = authService.select_user(username)
    if(loginResp == False):
        authService.create_user(username, password)
        flash("Successfully created the user, you can now sign in!")
    else:
        flash("Username is already taken")

@login_manager.user_loader
def load_user(user_id):
    resp = authService.get_user_by_id(user_id)
    if(resp != False):
        return resp
    return None