from app import config, tokens
from app.sensors.AirlySensor import AirlySensor
from app.sensors.HumidSensor import HumidSensor
from app.sensors.MockedSensor import MockedSensor
from app.sensors.PmSensor import PmSensor


def create_sensors():
    return [
        HumidSensor(config.SENSOR_NAME_HUMID_1, config.SENSOR_PORT_HUMID_1),
        PmSensor(config.SENSOR_NAME_PM, config.SENSOR_PORT_PM),
        AirlySensor(sensor_name=config.SENSOR_AIRLY_NAME, token=tokens.airly,
                    installation_id=config.SENSOR_AIRLY_INSTALLATION_ID)
    ]


def create_mocked_sensors():
    return [
        MockedSensor("mocked sensor 1"),
        MockedSensor("mocked sensor 2"),
        AirlySensor(sensor_name=config.SENSOR_AIRLY_NAME, token=tokens.airly,
                    installation_id=config.SENSOR_AIRLY_INSTALLATION_ID)
    ]
