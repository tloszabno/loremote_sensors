import sys
from loremote_sensors.main import main



if __name__ == '__main__':
    main(mocked=(len(sys.argv) > 1 and sys.argv[1] == "--mocked"))
