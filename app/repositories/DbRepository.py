from app.shared.measurement import MeasurementsSet
import sqlite3


class DbRepository(object):
    def __init__(self, path):
        self.path = path
        self.__init_db__()

    def save(self, measurement: MeasurementsSet):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()

            for value in measurement.values:
                parameters = (
                    measurement.id,
                    measurement.timestamp,
                    value.sensor_name,
                    value.measurement_name,
                    value.value,
                    value.unit,
                    value.timestamp
                )
                cursor.execute('''INSERT INTO 
                MEASUREMENTS(
                    MEASUREMENTS_SET_ID,
                    MEASUREMENTS_SET_TIMESTAMP,
                    SENSOR_NAME,
                    MEASUREMENT_NAME,
                    VALUE,
                    UNIT,
                    TIMESTAMP
                ) 
                VALUES(?,?,?,?,?,?)''', parameters)

    def __init_db__(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            print("__init_db__ creating table if not created before")
            cursor.execute('''CREATE TABLE IF NOT EXISTS MEASUREMENT_VALUES
                  (ID                           INT PRIMARY KEY AUTOINCREMENT,
                  MEASUREMENTS_SET_ID           TEXT    NOT NULL,
                  MEASUREMENTS_SET_TIMESTAMP    TEXT    NOT NULL,
                  MEASUREMENT_NAME              REAL    NOT NULL,
                  SENSOR_NAME                   REAL    NOT NULL,
                  VALUE                         REAL    NOT NULL,
                  UNIT                          REAL    NOT NULL,
                  TIMESTAMP                     TEXT    NOT NULL);''')
            conn.commit()
