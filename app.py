from app.shared.measurement import Measurement


def main():
    m = Measurement("some sensor", "humidity", 0.9, "%")


if __name__ == "__main__":
    main()
