from datetime import datetime, date


class PmMeasurement(object):
    def __init__(self, pm10, pm2_5, time=str(datetime.now())):
        self.time = datetime.fromisoformat(time)
        self.pm10 = pm10
        self.pm2_5 = pm2_5

    def __str__(self):
        return "PmMeasurement(pm10=%s, pm2_5=%s, time=%s)" % (str(self.pm10), str(self.pm2_5), str(self.time))
