import RPi.GPIO as GPIO
import Adafruit_DHT
import time
print("=== DHT11 TEST ===")
print("Connect G SV 24 25 to G VS N of DHT11")
GPIO.setmode(GPIO.BCM)
dhtPin = 24
sensor = Adafruit_DHT.DHT11
try:
 while True:
 humidity, temperature = Adafruit_DHT.read_retry(sensor, dhtPin)
 print("Humidity: ", humidity, "Temperature:", temperature)
 time.sleep(0.25)
except KeyboardInterrupt:
 GPIO.cleanup()
