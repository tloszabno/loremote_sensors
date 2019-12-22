from dataclasses import dataclass
from datetime import datetime


@dataclass
class Measurement(object):
    sensor_name: str
    measurement_name: str
    value: float
    unit: str
    timestamp: datetime = datetime.now()

    def to_json(self):
        return {
            "sensor_name": self.sensor_name,
            "measurement_name": self.measurement_name,
            "value": str(self.value),
            "unit": str(self.unit),
            "timestamp": str(self.timestamp)
        }
