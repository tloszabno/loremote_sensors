from app.google.SpreadSheets import get_connection_to_g_api
from app.measurement.Measurement import MeasurementsSet
from app.listeners.Listener import Listener
from app import config
import logging

logger = logging.getLogger('SpreadSheetUpdateListener')

class SpreadSheetUpdateListener(Listener):
    def notify(self, measurement: MeasurementsSet):
        try:
            gapi = get_connection_to_g_api()
            spreadsheet = gapi.open_by_key(config.SPREAD_SHEET_ID)
            by_measurements = {}
            for value in measurement.values:
                row = [value.sensor_name, value.timestamp.isoformat(), value.value, value.unit ]
                if value.measurement_name in by_measurements:
                    by_measurements[value.measurement_name].extend(row)
                else:
                    by_measurements[value.measurement_name] = row

            for measurement, row in by_measurements.items():
                wks = spreadsheet.worksheet(measurement)
                wks.append_row(row)
        except Exception as e:
            error = str(e)
            logger.exception(error)
