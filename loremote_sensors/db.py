import sqlite3

from loremote_sensors.config import db_path
from loremote_sensors.dto import PmMeasurement


class MeasurementsDAO(object):
    def __init__(self, path=db_path):
        self.path = path
        self.__init_db__()

    def save_pm_measurement(self, measurement):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO PM_MEASUREMENTS(PM10, PM25, TIME) VALUES (?, ?, ?)''',
                           (measurement.pm10, measurement.pm2_5, measurement.time))
            conn.commit()
            print("save_pm_measurement: saved %s" % str(measurement))

    def get_last_pm_measurements(self, max=10):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            results = []
            for row in cursor.execute('''SELECT PM10, PM25, TIME from PM_MEASUREMENTS order by TIME desc limit ?''',
                                      (max,)):
                results.append(PmMeasurement(pm10=row[0], pm2_5=row[1], time=row[2]))
            return results

    def __init_db__(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            print("__init_db__ creating table if not created before")
            cursor.execute('''CREATE TABLE IF NOT EXISTS PM_MEASUREMENTS
                 (ID INT PRIMARY KEY,
                 PM10   REAL    NOT NULL,
                 PM25   REAL    NOT NULL,
                 TIME   TEXT,
                 MARKS  INT);''')
            conn.commit()
