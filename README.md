# raspi-dht22-docker
Read temperature and humidity from DHT22 attached to Raspberry Pi running inside Docker and send to io.adafruit

## How to:

- Configure the DHT_DATA_PIN inside `temp_humidity.py`
- Add your ADAFRUIT_IO_KEY, ADAFRUIT_IO_USERNAME and Adafruit IO Feeds to `temp_humidity.py`
- Build image with `docker-compose build`
- Bring up app with `docker-compose up -d`
