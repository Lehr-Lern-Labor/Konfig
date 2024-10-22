###Imports###
from machine import Pin
from random import randint
from time import sleep



###Variablen###
#led_red verweist auf den Pin an dem eine rote LED angeschlossen ist, z.B. 18
led_red = Pin("""TODO""", Pin.OUT)
#led_ylw verweist auf den Pin an dem eine gelbe LED angeschlossen ist, z.B. 19
led_ylw = Pin("""TODO""", Pin.OUT)
#led_grn verweist auf den Pin an dem eine grüne LED angeschlossen ist, z.B. 20
led_grn = Pin("""TODO""", Pin.OUT)

#Die jeweiligen buttons verweisen auf entsprechende Pins an denen ein Knopf angeschlossen ist, z.B. 15
btn_red = Pin("""TODO""", Pin.IN, Pin.PULL_DOWN)
btn_ylw = Pin("""TODO""", Pin.IN, Pin.PULL_DOWN)
btn_grn = Pin("""TODO""", Pin.IN, Pin.PULL_DOWN)

#Es werden auch noch Variablen für den Spielzustand benötigt:
#Punktzahl, Liste mit lichtern, wird gerade gespielt?



###Code###
def add_random(current_list):
    new_entry = randint(0,2)
    if new_entry == 0: 
            current_list.append("red")
    elif new_entry == 1:
            current_list.append("ylw")
    elif new_entry == 2:
            current_list.append("grn")


#Geht durch die Liste von Lichtern durch und lässt jedes entsprechende Licht für die Länge von time_per_light aufleuchten.
#Hinweis: Durch Verwenden von global, können variablen im Variablen-Bereich in einer Methode verwendet werden.
#         Andernfalls würde es nicht funktionieren, da das Programm fälschlicherweise eine neue Variable erstellen würde.
def show_lights(time_per_light):
    #Beispiel für Hinweis: global name_der_variable
    #TODO

#Signalisiert dem Spieler auf eindeutige Weise, dass dieser verloren hat. Dann wird der Spielzustand geändert und es wird
#die Punktzahl ausgegeben.
def fail():
    #TODO

#Geht durch die Liste mit den Lichtern und wartet für jeden Eintrag auf eine Eingabe. Für jede getätigte Eingabe wird geprüft, 
#ob diese passend zum Listeneintrag gewählt wurde. Falls dies nicht der Fall gewesen sein sollte, wird fail aufgerufen.
def repeat_lights():
    #TODO
    
#Setzt den Spielzustand zurück und startet ein neues Spiel.
def restart():
    #TODO
    
### Sequence begins here ###
#Es wird solange der Spielablauf wiederholt, wie das Programm sich in einem spielenden Zustand befindet.
#Hinweis: Der Ablauf wäre wohlmöglich. show_lights, repeat_lights und Punktestand erhöhen.
#Wenn man mag, kann man auch time_per_light leicht verringern
def play():
    #TODO

restart()

