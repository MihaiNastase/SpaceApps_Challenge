from flaskext.mysql import MySQL
class db:
    def __init__(self, app):
        if(not hasattr(self, 'conn')):
            self.connect_db(app)
    
    def connect_db(self, app):
        mysql = MySQL()
        mysql.init_app(app)
        self.conn = mysql.connect()
        self.create_tables()

    def create_tables(self):
        drop_user_sql = "DROP TABLE IF EXISTS users;"
        drop_log_sql = "DROP TABLE IF EXISTS log;"
        
        create_user_sql = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(256),
            password TEXT
        );"""
        create_log_sql = """
        CREATE TABLE IF NOT EXISTS log (
            id SERIAL PRIMARY KEY,
            user_id INTEGER(11),
            message_text TEXT,
            verified INT(1),
            creation_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            modification_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        );"""

        cursor = self.conn.cursor()
        cursor.execute(drop_user_sql)
        cursor.execute(drop_log_sql)
        self.conn.commit()
        cursor.execute(create_user_sql)
        cursor.execute(create_log_sql)
        self.conn.commit()
        cursor.close()

