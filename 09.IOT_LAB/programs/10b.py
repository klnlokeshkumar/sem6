import RPi.GPIO as GPIO
import time
def distance(trigpin, echopin):
    GPIO.output(trigpin, True)
    time.sleep(0.0001)
    GPIO.output(trigpin, False)
    while GPIO.input(echopin) == 0:
    pulse_start = time.time()
    while GPIO.input(echopin) == 1:
    pulse_end = time.time()
    
    try:
    pulse_duration = pulse_end - pulse_start
    except:
    print('Calibrating')
    return -1
    
    distance = pulse_duration * 17150
    distance = round(distance + 1.15, 2)
    
    return distance
GPIO.setmode(GPIO.BCM)
trigpin = 24
echopin = 25
GPIO.setup(trigpin, GPIO.OUT)
GPIO.setup(echopin, GPIO.IN)
while True:
    dist = distance(trigpin, echopin)
    print('Measured distance = {}cm'.format(dist))
    time.sleep(0.01)
