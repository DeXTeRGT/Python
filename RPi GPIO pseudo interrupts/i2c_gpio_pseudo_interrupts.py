from signal import signal, SIGINT
from sys import exit
from pcf8574 import PCF8574

import RPi.GPIO as GPIO

i2c_bus = PCF8574(1, 0x20)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)

i2c_bus.port=[True, True, True, True, True, True, True, True]

def printFunction(channel):
    print("INT triggered")
    print(i2c_bus.port)
    i2c_bus.port=[True, True, True, True, True, True, True, True]
    
GPIO.add_event_detect(4, GPIO.FALLING, callback=printFunction, bouncetime=100)

def handler(signal_received, frame):
    GPIO.cleanup()
    print('Exiting the process')
    exit(0)
    

if __name__ == '__main__':
    signal(SIGINT, handler)
    print('Running the process')
    while True:
        pass
#signal.signal(signal.SIGINT, signal_handler)