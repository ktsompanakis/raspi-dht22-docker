"""
'temp_humidity.py'
==================================
Example of sending analog sensor
values to an Adafruit IO feed.

Author(s): Brent Rubell

Tutorial Link: Tutorial Link: https://learn.adafruit.com/adafruit-io-basics-temperature-and-humidity

Dependencies:
    - Adafruit IO Python Client
        (https://github.com/adafruit/io-client-python)
    - Adafruit_Python_DHT
        (https://github.com/adafruit/Adafruit_Python_DHT)
"""

# import standard python modules.
import time

# import adafruit dht library.
import Adafruit_DHT

# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed

# Delay in-between sensor readings, in seconds.
DHT_READ_TIMEOUT = 30

# Pin connected to DHT22 data pin
DHT_DATA_PIN = 4

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = '{YOUR_ADAFRUIT_IO_KEY}'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username).
ADAFRUIT_IO_USERNAME = '{YOUR_ADAFRUIT_IO_USERNAME}'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Set up Adafruit IO Feeds.
temperature_feed = aio.feeds('{YOUR_TEMPERATURE_FEED}')
humidity_feed = aio.feeds('{YOUR_HUMIDITY_FEED}')

# Set up DHT22 Sensor.
dht22_sensor = Adafruit_DHT.DHT22

# Set initial values
prev_hum, prev_temp = Adafruit_DHT.read_retry(dht22_sensor, DHT_DATA_PIN)
print('Initial Values: Temp={0:0.1f}*C | Humidity={1:0.1f}%'.format(prev_temp, prev_hum))

while True:
    timestamp = time.ctime()
    humidity, temperature = Adafruit_DHT.read_retry(dht22_sensor, DHT_DATA_PIN)
    if abs(humidity - prev_hum) < 10 and abs(temperature - prev_temp) < 10:
        print('Timestamp={0} | Temp={1:0.1f}*C | Humidity={2:0.1f}%'.format(timestamp, temperature, humidity))

        # Store values
        prev_hum = humidity
        prev_temp = temperature

        # Send humidity and temperature feeds to Adafruit IO
        temperature = '%.2f'%(temperature)
        humidity = '%.2f'%(humidity)
        aio.send(temperature_feed.key, str(temperature))
        aio.send(humidity_feed.key, str(humidity))
    else:
        print('Failed to get DHT22 Reading, trying again in ', DHT_READ_TIMEOUT, 'seconds')

    # Timeout to avoid flooding Adafruit IO
    time.sleep(DHT_READ_TIMEOUT)
