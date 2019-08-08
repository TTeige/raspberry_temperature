import datetime
import sqlite3


class TemperatureStorage:
    def __init__(self):
        self.conn = sqlite3.connect('temperature.db')
        c = self.conn.cursor()
        c.execute(
            'CREATE TABLE IF NOT EXISTS temperature (id integer primary key, temperature REAL, time TEXT, type TEXT)')
        c.close()

    def store(self, temperature, temperature_type):
        c = self.conn.cursor()
        time = datetime.datetime.now().isoformat()
        c.execute('INSERT INTO temperature (temperature, time, type) VALUES (?, ?, ?)',
                  (temperature, time, temperature_type))
        data = c.lastrowid
        self.conn.commit()
        c.close()
        return data

    def get_between(self, time_before, time_after, temperature_type):
        c = self.conn.cursor()
        c.execute('SELECT * FROM temperature WHERE datetime(time) BETWEEN ? AND ? AND type like ?',
                  (time_before, time_after, temperature_type))
        data = c.fetchall()
        c.close()
        return data

    def get_all(self, temperature_type):
        c = self.conn.cursor()
        c.execute('SELECT * FROM temperature WHERE type=?', (temperature_type,))
        data = c.fetchall()
        c.close()
        return data

    def get_by_id(self, id):
        c = self.conn.cursor()
        c.execute('SELECT * FROM temperature WHERE id=?', (id,))
        data = c.fetchall()
        c.close()
        return data

    def get_both(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM temperature')
        data = c.fetchall()
        c.close()
        return data
