from datetime import datetime
import dateutil.parser


class PmMeasurement(object):
    def __init__(self, pm10, pm2_5):
        self.pm10 = pm10
        self.pm2_5 = pm2_5

    def as_json(self):
        return {
            "pm10": str(self.pm10),
            "pm2_5": str(self.pm2_5)
        }

    def __str__(self):
        return "PmMeasurement(pm10=%s, pm2_5=%s)" % (str(self.pm10), str(self.pm2_5))

    def __eq__(self, other):
        if not other:
            return False
        if other.pm10 != self.pm10:
            return False
        if other.pm2_5 != self.pm2_5:
            return False
        return True


class HumidMeasurement(object):
    def __init__(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity

    def as_json(self):
        return {
            "temperature": str(self.temperature),
            "humidity": str(self.humidity),
        }

    def __str__(self):
        return "HumidMeasurement(temperature=%s, humidity=%s)" % (str(self.temperature), str(self.humidity))

    def __eq__(self, other):
        if not other:
            return False
        if other.humidity != self.humidity:
            return False
        if other.temperature != self.temperature:
            return False
        return True


class Measurement(object):
    def __init__(self, pm, humid1, humid2, time=None):
        self.time = dateutil.parser.parse(time) if time else datetime.now()
        self.pm = pm
        self.humid1 = humid1
        self.humid2 = humid2

    def as_json(self):
        return {
            "humid_1": self.humid1.as_json(),
            "humid_2": self.humid2.as_json(),
            "pm": self.pm.as_json(),
            "time": str(self.time)
        }

    def __str__(self):
        return "Measurement(pm=%s, humid1=%s, humid2=%s, time=%s)" % (str(self.pm), str(self.humid1), str(self.humid2), str(self.time))

    def __eq__(self, other):
        if not other:
            return False
        if other.time != self.time:
            return False
        if other.humid1 != self.humid1:
            return False
        if other.humid2 != self.humid2:
            return False
        if other.pm != self.pm:
            return False
        return True
