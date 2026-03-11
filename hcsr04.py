from hcsr04 import HCSR04
from time import sleep
from machine import Pin

# ESP32
sensor = HCSR04(trigger_pin=18, echo_pin=19, echo_timeout_us=10000)
led = Pin(2,Pin.OUT)

# ESP8266
#sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)

while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    
    if distance < 20:
        led.value(1)
        
    else:
        led.value(0)
        
    sleep(0.2)
