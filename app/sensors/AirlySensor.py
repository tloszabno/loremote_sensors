from typing import List

import requests

from app.sensors.Sensor import Sensor
from app.measurement.Measurement import Measurement, MeasurementTypes, MeasurementUnits


class AirlySensor(Sensor):
    def __init__(self, sensor_name, token, installation_id):
        self.senor_name = sensor_name
        self.token = token
        self.installation_id = installation_id

    def measure(self) -> List[Measurement]:
        pm25, pm10, temp, humidity, error = 0.0, 0.0, 0.0, 0.0, ""
        try:
            headers = {'apikey': self.token, 'Accept': 'application/json'}
            response = requests.get(
                'https://airapi.airly.eu/v2/measurements/installation?installationId=' + self.installation_id,
                headers=headers).json()
            current = response['current']['values']
            pm25 = get_value(current, 'PM25')
            pm10 = get_value(current, 'PM10')
            temp = get_value(current, 'TEMPERATURE')
            humidity = get_value(current, 'HUMIDITY')
        except Exception as e:
            error = str(e)

        measurements = [
            Measurement(sensor_name=self.senor_name,
                        measurement_name=MeasurementTypes.TEMPERATURE,
                        unit=MeasurementUnits.TEMPERATURE,
                        value=temp, error=error),
            Measurement(sensor_name=self.senor_name,
                        measurement_name=MeasurementTypes.HUMIDITY,
                        unit=MeasurementUnits.HUMIDITY,
                        value=humidity, error=error),
            Measurement(sensor_name=self.senor_name,
                        measurement_name=MeasurementTypes.PM_10,
                        unit=MeasurementUnits.AIR_POLLUTION,
                        value=pm10, error=error),
            Measurement(sensor_name=self.senor_name,
                        measurement_name=MeasurementTypes.PM_2_5,
                        unit=MeasurementUnits.AIR_POLLUTION,
                        value=pm25, error=error),
        ]
        return measurements


def get_value(value_list, name):
    return list(filter(lambda entry: entry['name'] == name, value_list))[0]['value']
