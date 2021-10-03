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
        drop_log_sql = "DROP TABLE IF EXISTS logs;"
        
        create_user_sql = """
        CREATE TABLE IF NOT EXISTS users (
            id VARCHAR(20) PRIMARY KEY ,
            password TEXT
        );"""
        create_log_sql = """
        CREATE TABLE IF NOT EXISTS logs (
            id INT(11) PRIMARY KEY AUTO_INCREMENT,
            user_id VARCHAR(20) NOT NULL,
            message_text TEXT,
            verified INT(1),
            creation_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            modification_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );"""

        cursor = self.conn.cursor()
        cursor.execute(drop_log_sql)
        cursor.execute(drop_user_sql)
        self.conn.commit()
        cursor.execute(create_user_sql)
        cursor.execute(create_log_sql)
        self.conn.commit()
        cursor.close()

    def add_logs(self):
        add_logs_sql ="""
        INSERT INTO `logs` (`id`, `user_id`, `message_text`, `verified`, `creation_datetime`, `modification_datetime`) 
        VALUES 
            (NULL, 'admin', 'This is log 1', NULL, current_timestamp(), current_timestamp()), 
            (NULL, 'admin', 'This is log 2', NULL, current_timestamp(), current_timestamp()), 
            (NULL, 'admin', 'This is log 3', NULL, current_timestamp(), current_timestamp());
        """
        cursor = self.conn.cursor()
        cursor.execute(add_logs_sql)
        self.conn.commit()
        cursor.close()

    def get_logs(self):
        get_logs_sql = """SELECT * FROM logs"""
        cursor = self.conn.cursor()
        cursor.execute(get_logs_sql)
        data = cursor.fetchall()
        cursor.close()

        return data