from typing import List

from app import tokens
from app.sensors.Sensor import Sensor
from app.shared.measurement import Measurement
import requests


class AirlySensor(Sensor):
    def __init__(self, sensor_name):
        self.senor_name = sensor_name

    def measure(self) -> List[Measurement]:
        headers = {'apikey': tokens.airly, 'Accept': 'application/json'}
        response = requests.get('https://airapi.airly.eu/v2/measurements/installation?installationId=9899',
                                headers=headers).json()
        current = response['current']['values']
        pm25 = get_value(current, 'PM25')
        pm10 = get_value(current, 'PM10')
        temp = get_value(current, 'TEMPERATURE')
        humidity = get_value(current, 'HUMIDITY')
        measurements = [
            Measurement(sensor_name=self.senor_name,
                        measurement_name="temperature",
                        unit="C",
                        value=temp),
            Measurement(sensor_name=self.senor_name,
                        measurement_name="humidity",
                        unit="%",
                        value=humidity),
            Measurement(sensor_name=self.senor_name,
                        measurement_name="pm_10",
                        unit="ug/m^3",
                        value=pm10),
            Measurement(sensor_name=self.senor_name,
                        measurement_name="pm_2.5",
                        unit="ug/m^3",
                        value=pm25),
        ]
        print(measurements)
        return measurements


def get_value(value_list, name):
    return list(filter(lambda entry: entry['name'] == name, value_list))[0]['value']
