from datetime import datetime
from typing import Mapping
from flask import json, jsonify

class LogModel:
    
    user_id: str
    message_text: str
    time_stamp: str

    def __init__(self, user_id: str, message_text: str):
        self.user_id = user_id
        self.message_text = message_text
        self.time_stamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)


def main():
    log: LogModel = LogModel("mihai_11", "Huston, we have a problem")
    print(log.toJson())



if __name__ == "__main__":
    main()