from db import db
from flask_bcrypt import Bcrypt
class authService:

    def __init__(self, app):
        if(not hasattr(self, 'conn')):
            self.db = db(app)
        self.bcrypt = Bcrypt(app)

    def create_user(self, username, password):
        pw_hash = self.bcrypt.generate_password_hash(password).decode('utf-8')
        cursor = self.db.conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, pw_hash))
        self.db.conn.commit()
        cursor.close()

    def create_log(self, user_id, message_text, verified):
        cursor = self.db.conn.cursor()
        cursor.execute("INSERT INTO log (user_id, message_text, verified) VALUES (%s, %s, %s)", (user_id, message_text, verified))
        self.db.conn.commit()
        cursor.close()

        


