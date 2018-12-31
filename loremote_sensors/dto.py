from datetime import datetime
import dateutil.parser

class PmMeasurement(object):
    def __init__(self, pm10, pm2_5, time=None):
        self.time = dateutil.parser.parse(time) if time else datetime.now()
        self.pm10 = pm10
        self.pm2_5 = pm2_5

    def as_json(self):
        return {
            "pm10": str(self.pm10),
            "pm2_5": str(self.pm2_5),
            "time": str(self.time)
        }

    def __str__(self):
        return "PmMeasurement(pm10=%s, pm2_5=%s, time=%s)" % (str(self.pm10), str(self.pm2_5), str(self.time))

    def __eq__(self, other):
        if not other:
            return False
        if other.time != self.time:
            return False
        if other.pm10 != self.pm10:
            return False
        if other.pm2_5 != self.pm2_5:
            return False
        return True
