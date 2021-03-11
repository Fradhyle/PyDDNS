import sqlite3


class DataMan:
    def __init__(self):
        self.db_file = 'data.db'

    def connect(self):
        try:
            conn = sqlite3.connect(self.db_file)
        except sqlite3.Error as e:
            print(e)
        else:
            return conn
