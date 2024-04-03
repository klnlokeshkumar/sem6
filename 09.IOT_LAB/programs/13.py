import urllib.request
import time
import RPi.GPIO as GPIO
import Adafruit_DHT
writeAPIKey = 'FNAIGOOVH990KRLW'
baseURL = "https://api.thingspeak.com/update?api_key={}".format(writeAPIKey)
sensor = Adafruit_DHT.DHT11
sensorPin = 18
GPIO.setmode(GPIO.BCM)
try:
 while True:
 humidity, temperature = Adafruit_DHT.read_retry(sensor, sensorPin)
 if humidity is not None and temperature is not None:
 humidity = '{:.2f}'.format(humidity)
 temperature = '{:.2f}'.format(temperature) 
 conn = urllib.request.urlopen(baseURL + '&field1={}&field2={}'.format(humidity, 
temperature))
 print(conn.read())
 conn.close()
 time.sleep(20)
except KeyboardInterrupt:
 GPIO.cleanup()
 exit()
