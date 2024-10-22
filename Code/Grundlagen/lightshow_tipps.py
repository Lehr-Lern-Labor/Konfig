###Imports###
from machine import Pin
from time import sleep
from random import randint
###Variablen###
led_red = Pin("""TODO: Pin Nummer hier einfügen""",Pin.OUT)
led_ylw = Pin("""TODO: Pin Nummer hier einfügen""",Pin.OUT)
led_grn = Pin("""TODO: Pin Nummer hier einfügen""",Pin.OUT)
light_list = []
wait_time = 1
#btn_red = Pin("""TODO: Pin Nummer hier einfügen""", Pin.IN, Pin.PULL_DOWN)
#btn_ylw = Pin("""TODO: Pin Nummer hier einfügen""", Pin.IN, Pin.PULL_DOWN)
#btn_grn = Pin("""TODO: Pin Nummer hier einfügen""", Pin.IN, Pin.PULL_DOWN)
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

def play_light(light):
    if light == "red":
        sleep(wait_time)
        led_red.toggle()
        sleep(wait_time)
        led_red.toggle()
    #TODO: gelbe und grüne LED einfügen

def add_light(current_list,light):
    #TODO: light an current_list anhängen
    
def add_random(current_list):
    new_entry = randint(0,2)
    if new_entry == 0: # match case im Moment leider nicht unterstüzt
            current_list.append("red")
    #TODO: gelbe und grüne LED hinzufügen

def add_per_button(current_list):
    while not (btn_red.value() or btn_ylw.value() or btn_grn.value()):
        sleep(0.01)
    if btn_red.value():
        led_red.toggle()
        while btn_red.value():
            sleep(0.01)
        led_red.toggle()
        current_list.append("red")
    #TODO: gelbe und grüne LED hinzufügen