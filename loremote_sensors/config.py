from enum import Enum

class IntervalsConfig:
    MEASURE_INTERVAL_IN_MIN = 10 #refactor


pmsensor_port = "/dev/ttyUSB0"
db_path = "loremote_sensors.sqlite"


class HumidSensor(Enum):
    SENSOR_1 = 1,
    SENSOR_2 = 2

humid_sensor_port = dict()
humid_sensor_port[HumidSensor.SENSOR_1] = "15"
humid_sensor_port[HumidSensor.SENSOR_2] = "24"
