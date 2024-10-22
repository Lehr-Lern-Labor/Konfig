###Imports###
from machine import Pin
from time import sleep



###Variablen###
#led verweist auf die onboard LED
led = Pin("""TODO""",Pin.OUT)
#button verweist auf den Pin an dem ein Knopf angeschlossen ist, z.B. 15
button = Pin("""TODO""", Pin.IN, Pin.PULL_DOWN)



###Code###
#Die LED leuchtet solange wie der Knopf gedrückt wird.
#Wird der Knopf losgelassen, hört die LED auch wieder mit dem leuchten auf.
while True:
    if button.value():
        #TODO
        
