import sqlite3

from loremote_sensors.config import db_path
from loremote_sensors.dto import Measurement, PmMeasurement, HumidMeasurement


class MeasurementsDAO(object):
        def __init__(self, path=db_path):
            self.path = path
            self.__init_db__()

        def save_measurement(self, measurement):
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                cursor.execute('''INSERT INTO MEASUREMENTS_V2(PM10, PM25, TEMPERATURE_1, HUMIDITY_1, TEMPERATURE_2, HUMIDITY_2, TIME) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                               (measurement.pm.pm10, measurement.pm.pm2_5, measurement.humid1.temperature, measurement.humid1.humidity, measurement.humid2.temperature, measurement.humid2.humidity, measurement.time))
                conn.commit()
                print("save_measurement: saved %s" % str(measurement))

        def get_last_measurements(self, max=10):
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                results = []
                for row in cursor.execute('''SELECT PM10, PM25, TEMPERATURE_1, HUMIDITY_1, TEMPERATURE_2, HUMIDITY_2, TIME from MEASUREMENTS_V2 order by TIME desc limit ?''',
                                          (max,)):
                    humid1 = HumidMeasurement(temperature=row[2], humidity=row[3])
                    humid2 = HumidMeasurement(temperature=row[4], humidity=row[5])
                    pm = PmMeasurement(pm10=row[0], pm2_5=row[1])
                    results.append(Measurement(pm=pm, humid1=humid1,
                                               humid2=humid2, time=row[6]))
                return results

        def __init_db__(self):
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                print("__init_db__ creating table if not created before")
                cursor.execute('''CREATE TABLE IF NOT EXISTS MEASUREMENTS_V2
                     (ID INT PRIMARY KEY,
                     PM10   REAL    NOT NULL,
                     PM25   REAL    NOT NULL,
                     TEMPERATURE_1   REAL    NOT NULL,
                     HUMIDITY_1   REAL    NOT NULL,
                     TEMPERATURE_2   REAL    NOT NULL,
                     HUMIDITY_2   REAL    NOT NULL,
                     TIME   TEXT,
                     MARKS  INT);''')
                conn.commit()
