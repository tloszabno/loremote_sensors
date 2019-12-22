from app.measurement.MeasurementService import MeasurementService
from app.shared.measurement import MeasurementsSet


def main():
    m = MeasurementsSet("some sensor", "humidity", 0.9, "%")
    measurement_service = MeasurementService()



if __name__ == "__main__":
    main()
