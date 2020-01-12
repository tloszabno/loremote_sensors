import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Measurement(object):
    sensor_name: str
    measurement_name: str
    unit: str
    value: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)
    error: str = ""

    def to_json(self):
        return {
            "sensor_name": self.sensor_name,
            "measurement_name": self.measurement_name,
            "value": str(round(self.value, 2)),
            "unit": str(self.unit),
            "timestamp": self.timestamp.isoformat(),
            "error": self.error
        }


@dataclass
class MeasurementsSet(object):
    values: List[Measurement]
    timestamp: datetime = field(default_factory=datetime.now)
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def to_json(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp.isoformat(),
            "measurements": [x.to_json() for x in self.values]
        }

    def get_all_with_name(self, measurement_name):
        return list(filter(lambda x: x.measurement_name == measurement_name, self.values))


class MeasurementUnits(object):
    TEMPERATURE = "C"
    HUMIDITY = "%"
    AIR_POLLUTION = "ug/m^3"
    PRESSURE = "hPa"


class MeasurementTypes(object):
    TEMPERATURE = "temperature"
    HUMIDITY = "humidity"
    PRESSURE = "pressure"
    PM_10 = "pm 10"
    PM_2_5 = "pm 2.5"
