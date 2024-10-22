###Imports###
from machine import Pin
from time import sleep



###Variablen###
#led verweist auf die onboard LED
led = Pin("""TODO""",Pin.OUT)
#button verweist auf den Pin an dem ein Knopf angeschlossen ist, z.B. 15
button = Pin("""TODO""", Pin.IN, Pin.PULL_DOWN)



###Code###
#Es wird durchgehend geprüft, ob der Knopf gerade gedrückt wird.
#Wenn der Knopf gerade gedrückt wird, soll die LED zwischen an und aus wechseln (toggle).
#Bonus: Warum ist der Aufruf von sleep wichtig? Was könnte sonst passieren?
while True:
    if button.value():
        #TODO
        sleep(0.5)
