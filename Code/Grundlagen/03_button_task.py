###Imports###
from machine import Pin
from time import sleep



###Variablen###
#led verweist auf die onboard LED
led = Pin("""TODO""",Pin.OUT)
#button verweist auf den Pin an dem ein Knopf angeschlossen ist, z.B. 15
button = Pin("""TODO""", Pin.IN, Pin.PULL_DOWN)

#Möglicherweise musst du dir noch eine Variable mit einem Wahrheitswert definieren, z.B. a = True oder b = False




###Code###
#Die LED soll solange blinken, bis einmal der Knopf gedrückt wird.
#Wenn der Knopf gerade gedrückt wird, hört die LED mit dem Blinken auf.
#Bonus: Es gibt zwei mögliche Ansätze, einen für den man eine Variable
#       definieren muss und einen für den das nicht notwendig ist.
#       Fallen dir beide ein? Kleiner Tipp: mit 'not' kann geprüft werden,
#       ob etwas nicht der Fall ist.
while #TODO:
    sleep(0.5)
    led.toggle()
    sleep(0.5)
    if button.value():
        #TODO
        
