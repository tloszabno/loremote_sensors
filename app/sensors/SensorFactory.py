from app import config
from app.sensors.HumidSensor import HumidSensor
from app.sensors.MockedSensor import MockedSensor
from app.sensors.PmSensor import PmSensor


def create_sensors():
    return [
        HumidSensor(config.SENSOR_NAME_HUMID_1, config.SENSOR_PORT_HUMID_1),
        HumidSensor(config.SENSOR_NAME_HUMID_2, config.SENSOR_PORT_HUMID_2),
        PmSensor(config.SENSOR_NAME_PM, config.SENSOR_PORT_PM)
    ]


def create_mocked_sensors():
    return [
        MockedSensor("mocked sensor 1"),
        MockedSensor("mocked sensor 2")
    ]
