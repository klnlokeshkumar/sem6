import RPi.GPIO as GPIO
import time
print("RGB LED TEST")
print("Connect 10 11 12 13 to G R Gr B of RGB LED")
i = input('Enter the color: ')
GPIO.setmode(GPIO.BCM)
buzzer = 14
commonCathode = 10
red = 11
green = 12
blue = 13
def ledColour(colour="none"):
 for x in range(10, 14):
 GPIO.setup(x, GPIO.OUT)
 GPIO.output(x, GPIO.LOW)
 if colour == "red":
 GPIO.output(red, GPIO.HIGH)
 elif colour == "green":
 GPIO.output(green, GPIO.HIGH)
 elif colour == "blue":
 GPIO.output(blue, GPIO.HIGH)
while True:
 ledColour(i)
 time.sleep(2)
