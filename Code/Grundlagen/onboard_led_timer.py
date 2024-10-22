###Imports###
from machine import Pin, Timer
###Variablen###
led = Pin("LED", Pin.OUT)
timer = Timer()
###Code###
def blink(timer):
    led.toggle()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
    