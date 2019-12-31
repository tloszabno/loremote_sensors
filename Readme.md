# Requirements (Raspberry PI zero)

```
sudo apt-get install python3-dev python3-rpi.gpio
sudo pip3 install Adafruit_DHT

```


BME 280 sensor configured according to http://www.whatimade.today/log-sensor-data-straight-to-google-sheets-from-a-raspberry-pi-zero-all-the-python-code/

1. enable I2C bus in `raspi-config`
2. `sudo apt-get install -y python3-smbus i2c-tools`