from app.measurement.Measurement import MeasurementsSet
from app.listeners.Listener import Listener
from app import config
import logging

class SpreadSheetUpdateListener(Listener):
    def __init__(self, gapi):
        self.gapi = gapi

    def notify(self, measurement: MeasurementsSet):
        try:
            spreadsheet = self.gapi.open_by_key(config.SPREAD_SHEET_ID)
            by_measurements ={}

            for value in measurement.values:
                row = [value.sensor_name, value.timestamp.isoformat(), value.value, value.unit ]
                if value.measurement_name in by_measurements:
                    by_measurements[value.measurement_name].append(row)
                else:
                    by_measurements[value.measurement_name] = [ row ]

            for measurement, rows in by_measurements.items():
                wks = spreadsheet.worksheet(measurement)
                for row in rows:
                    wks.append_row(row)
        except Exception as e:
            error = str(e)
            logger.exception(error)
