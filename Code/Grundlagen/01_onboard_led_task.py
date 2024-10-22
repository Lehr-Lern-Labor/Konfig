###Imports###
from machine import Pin
from time import sleep



###Variablen###
led = Pin("LED", Pin.OUT)



###Code###
#Die LED blinkt durchgehend
while True:
    led.value(1)
    sleep(0.5)
    #TODO
    
