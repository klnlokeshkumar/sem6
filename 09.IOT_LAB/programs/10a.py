import RPi.GPIO as GPIO
import time
print("BUZZER TEST")
print("Connect G 5V 24 25 to G V S N of Buzzer")
buzzerPin = 24 # Assign the correct GPIO pin number
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)
while True:
 GPIO.output(buzzerPin, GPIO.HIGH)
 time.sleep(0.381) # Adjust the sleep time as needed
 GPIO.output(buzzerPin, GPIO.LOW)
 time.sleep(0.381) # Adjust the sleep time as needed