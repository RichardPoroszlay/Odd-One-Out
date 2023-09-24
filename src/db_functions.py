from flask_mysqldb import MySQL
import random


class DbConnections:
    def __init__(self, app) -> None:
        self.app = app
        self.mysql = MySQL(app)

    def get_all_word(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT * FROM `Oddoneout`')
        data = cursor.fetchall()
        return data

    def get_random_record(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT * FROM `Oddoneout`')
        data = cursor.fetchall()
        if data:
            random_record = random.choice(data)
            return random_record
        else:
            return None