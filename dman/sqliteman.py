import sqlite3
import pathlib


class SQLMan:
    def __init__(self):
        self.db_file = pathlib.PurePath('../data.db')

    def connect(self):
        try:
            conn = sqlite3.connect(self.db_file)
        except sqlite3.Error as e:
            print(e)
        else:
            return conn