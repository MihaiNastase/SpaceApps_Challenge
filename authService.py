from db import db
from flask_bcrypt import Bcrypt
from user import user
class authService:

    def __init__(self, app):
        if(not hasattr(self, 'conn')):
            self.db = db(app)
        self.bcrypt = Bcrypt(app)

    def get_user_by_id(self, id):
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s LIMIT 1", (id))
        if(cursor.rowcount > 0):
            data = cursor.fetchone()
            data = user(data[0], data[1], data[2])
        else:
            data = False
        cursor.close()
        return data


    def create_user(self, username, password):
        pw_hash = self.bcrypt.generate_password_hash(password).decode('utf-8')
        cursor = self.db.conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, pw_hash))
        self.db.conn.commit()
        cursor.close()
    
    def select_user(self, username):
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s LIMIT 1", (username))
        if(cursor.rowcount > 0):
            data = cursor.fetchone()
            data = user(data[0], data[1], data[2])
        else:
            data = False
        cursor.close()
        return data

    def check_password_hash(self, password, passwordHash):
        return self.bcrypt.check_password_hash(passwordHash, password)

    def login(self, username, password):
        selectedUserData = self.select_user(username)
        if(selectedUserData != False):
            if(self.check_password_hash(password, selectedUserData.password)):
                return selectedUserData
            else:
                return False
        return False
        

    



