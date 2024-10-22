###Imports###
from machine import Pin
from time import sleep



###Variablen###
#onboard_led verweist auf die onboard LED
onboard_led = Pin("LED",Pin.OUT)
#led verweist auf den Pin an dem eine LED angeschlossen ist, z.B. 17
led = Pin("""TODO""", Pin.OUT)
#button verweist auf den Pin an dem ein Knopf angeschlossen ist, z.B. 15
button = Pin("""TODO""", Pin.IN, Pin.PULL_DOWN)

#Möglicherweise musst du dir noch eine Variable mit einem Wahrheitswert definieren, z.B. a = True oder b = False




###Code###
#Durch drücken des Knopfes soll man entscheiden können, ob gerade die externe LED oder die auf den Pico leuchtet.
#Bei jedem Knopfdruck soll zwischen onboard und extern gewechselt werden.
#Zunächst soll die onboard LED leuchten
while True:
    #TODO
    if button.value():
        #TODO
        sleep(0.25)
        
