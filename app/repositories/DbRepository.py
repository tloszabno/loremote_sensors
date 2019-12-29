import sqlite3

import dateutil.parser

from app.repositories.Repository import Repository
from app.shared.measurement import MeasurementsSet, Measurement


class DbRepository(Repository):
    def __init__(self, path):
        self.path = path
        self.__init_db__()

    def save(self, measurement: MeasurementsSet):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            for value in measurement.values:
                parameters = (
                    measurement.id,
                    measurement.timestamp.isoformat(),
                    value.sensor_name,
                    value.measurement_name,
                    value.value,
                    value.unit,
                    value.timestamp.isoformat(),
                    value.error
                )
                cursor.execute('''INSERT INTO MEASUREMENTS(
                    MEASUREMENTS_SET_ID,
                    MEASUREMENTS_SET_TIMESTAMP,
                    SENSOR_NAME,
                    MEASUREMENT_NAME,
                    VALUE,
                    UNIT,
                    TIMESTAMP,
                    ERROR
                ) 
                VALUES(?,?,?,?,?,?,?,?)''', parameters)
            conn.commit()

    def get_last(self, max=100):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            set_ids = list(map(lambda x: x[0], cursor.execute(
                '''SELECT DISTINCT MEASUREMENTS_SET_ID FROM MEASUREMENTS 
                order by MEASUREMENTS_SET_TIMESTAMP desc limit ?''',
                (max,))))
            sql = f'''
                SELECT 
                    MEASUREMENTS_SET_ID,
                    MEASUREMENTS_SET_TIMESTAMP,
                    MEASUREMENT_NAME,
                    SENSOR_NAME,
                    VALUE,
                    UNIT,
                    TIMESTAMP,
                    ERROR
                    FROM MEASUREMENTS where MEASUREMENTS_SET_ID in ({','.join(['?'] * len(set_ids))})
                    order by MEASUREMENTS_SET_TIMESTAMP
            '''
            measurement_sets = {}
            for row in cursor.execute(sql, set_ids):
                set_id = row[0]
                set_timestamp = dateutil.parser.parse(row[1])
                if set_id not in measurement_sets:
                    measurement_sets[set_id] = (set_timestamp, [])
                measurement_sets[set_id][1].append(Measurement(
                    sensor_name=row[3],
                    measurement_name=row[2],
                    value=row[4],
                    unit=row[5],
                    timestamp=dateutil.parser.parse(row[6]),
                    error=row[7]))
            return sorted([MeasurementsSet(values=value[1], timestamp=value[0], id=key) for key, value in
                           measurement_sets.items()], key=lambda x: x.timestamp)

    def __init_db__(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            print("__init_db__ creating table if not created before")
            cursor.execute('''CREATE TABLE IF NOT EXISTS MEASUREMENTS
                  (ID                           INTEGER PRIMARY KEY AUTOINCREMENT,
                  MEASUREMENTS_SET_ID           TEXT    NOT NULL,
                  MEASUREMENTS_SET_TIMESTAMP    TEXT    NOT NULL,
                  MEASUREMENT_NAME              REAL    NOT NULL,
                  SENSOR_NAME                   REAL    NOT NULL,
                  VALUE                         REAL    NOT NULL,
                  UNIT                          REAL    NOT NULL,
                  ERROR                         TEXT,
                  TIMESTAMP                     TEXT    NOT NULL);''')
            conn.commit()
