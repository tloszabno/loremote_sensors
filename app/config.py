# sensors
SENSOR_NAME_HUMID_1 = "humid home 1"
SENSOR_PORT_HUMID_1 = "15"

SENSOR_NAME_HUMID_2 = "humid home 2"
SENSOR_PORT_HUMID_2 = "24"

SENSOR_NAME_PM = "pm sensor"
SENSOR_PORT_PM = "/dev/ttyUSB0"

SENSOR_AIRLY_NAME = "Airly Slomczynskiego"
SENSOR_AIRLY_INSTALLATION_ID = "9899"

# db
DB_PATH = "measurements.sqlite"

# time
MEASURE_INTERVAL_IN_MIN = 10

# cache
DAYS_IN_CACHE = 1
ELEMENTS_IN_CACHE = (60 / MEASURE_INTERVAL_IN_MIN) * 24 * DAYS_IN_CACHE
