from db import db
class websocket:
    def __init__(self, app):
        if(not hasattr(self, 'conn')):
            self.db = db(app)

    def get_logs(self):
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM logs ORDER BY creation_datetime DESC")
        dataSet = []
        if(cursor.rowcount > 0):
            data = cursor.fetchall()
            for row in data:
                dataRow = { 
                    'id': str(row[0]), 
                    'userId': str(row[1]), 
                    'message_text': row[2],
                    'verified': str(row[3]),
                    'creation_datetime': str(row[4]),
                    'modification_datetime': str(row[5]),
                    }
                dataSet.append(dataRow)
        cursor.close()
        return dataSet

    def get_specific_log(self, id):
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM logs WHERE id = %s", id)
        dataRow = None
        if(cursor.rowcount > 0):
            data = cursor.fetchall()
            for row in data:
                dataRow = { 
                    'id': str(row[0]), 
                    'userId': str(row[1]), 
                    'message_text': row[2],
                    'verified': str(row[3]),
                    'creation_datetime': str(row[4]),
                    'modification_datetime': str(row[5]),
                }
        cursor.close()
        return dataRow

    def log_message(self, user_id, message_text, verified):
        cursor = self.db.conn.cursor()
        cursor.execute("INSERT INTO logs (user_id, message_text, verified) VALUES (%s, %s, %s)", (user_id, message_text, verified))
        cursor.close()
        return cursor.lastrowid
