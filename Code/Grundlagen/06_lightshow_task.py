###Imports###
from machine import Pin
from time import sleep
from random import randint



###Variablen###
#led_red verweist auf den Pin an dem eine rote LED angeschlossen ist, z.B. 18
led_red = Pin("""TODO""",Pin.OUT)
#led_ylw verweist auf den Pin an dem eine gelbe LED angeschlossen ist, z.B. 19
led_ylw = Pin("""TODO""",Pin.OUT)
#led_grn verweist auf den Pin an dem eine grüne LED angeschlossen ist, z.B. 20
led_grn = Pin("""TODO""",Pin.OUT)

light_list = []
wait_time = 1

#Die jeweiligen buttons verweisen auf entsprechende Pins an denen ein Knopf angeschlossen ist, z.B. 15
#btn_red = Pin("""TODO""", Pin.IN, Pin.PULL_DOWN)
#btn_ylw = Pin("""TODO""", Pin.IN, Pin.PULL_DOWN)
#btn_grn = Pin("""TODO""", Pin.IN, Pin.PULL_DOWN)



###Code###
def reset_lights():
    global light_list
    light_list = []

def play_lights():
    led_red.value(0)
    led_ylw.value(0)
    led_grn.value(0)
    for light in light_list:
        play_light(light)

#Beim Aufruf wird die über light mitgeteilte LED kurz zum Aufleuchten gebracht.
#Hinweis: 'light' ist ein Parameter und soll für ein beliebiges Licht stehen, dass übergeben werden kann.
#        Was genau light repräsentiert und für welches Licht die Werte stehen ist dir überlassen.
#        Beispielsweise kann light eine Zeichenfolge sein und "red" für die rote LED, "ylw" für die gelbe
#        LED und "grn" für die grüne LED stehen. Man könnte light aber auch als ganze Zahl verwenden, dann
#        stünde beispielsweise 0 für die rote LED, 1 für die gelbe LED und 2 für die grüne LED.
def play_light(light):
    #TODO

#Hängt den Eintrag light, an die current_list an.
#Hinweis: Durch Aufruf von append(Eintrag) auf eine Liste kann der übergebene Eintrag hinten angehängt werden.
def add_light(current_list,light):
    #TODO
    
#Hängt einen zufälligen Eintrag an die current_list an.
#Hinweis: new_entry ist eine zufällige Zahl zwischen 0 und 2.
#         Anhand von new_entry lässt sich eine LED bestimmen, die an current_list angehängt wird.
def add_random(current_list):
    new_entry = randint(0,2)
    #TODO

#Beim Aufruf wird auf eine Eingabe durch einen Knopfdruck gewartet. 
#Über diesen Knopfdruck wird die LED bestimmt, die an current_list angehängt wird.
#Am besten gibt man noch visuelle Rückmeldung, in dem man die gewählte LED kurz aufleuchten lässt.
#Hinweis: Man muss einen Weg finden, dass beim Knopfdruck nicht ausversehen mehrmals der gleiche
#         Eintrag angehangen wird. Man kann beispielsweise warten bis der Knopf losgelassen wird
#         und erst dann den Code weiter ausführen.
def add_per_button(current_list):
    while not (btn_red.value() or btn_ylw.value() or btn_grn.value()):
        sleep(0.01)
    #TODO 