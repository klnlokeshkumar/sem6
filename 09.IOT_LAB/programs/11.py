import RPi.GPIO as GPIO
import time
print("=== SERVO MOTOR TEST ===")
print("Connect G 5V 24 25 to G V S N of Servo")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
servoPin = 24
GPIO.setup(servoPin, GPIO.OUT)
p = GPIO.PWM(servoPin, 50)
p.start(0)
try:
 while True:
 for i in range(2, 11, 1):
 p.ChangeDutyCycle(1) # left -90 deg position
 time.sleep(0.5)
except KeyboardInterrupt:
 p.stop()
 GPIO.cleanup()
