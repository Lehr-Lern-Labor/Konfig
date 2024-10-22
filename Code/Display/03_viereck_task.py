#Imports
from machine import Pin, I2C

from ssd1306 import SSD1306_I2C
 
 
#Variablen
#buttons verweisen auf den Pin an dem ein Knopf angeschlossen ist, z.B. 15
btn_lft = Pin("""TODO""", Pin.IN, Pin.PULL_DOWN)
btn_rgt = Pin("""TODO""", Pin.IN, Pin.PULL_DOWN)
btn_dwn = Pin("""TODO""", Pin.IN, Pin.PULL_DOWN)
btn_up = Pin("""TODO""", Pin.IN, Pin.PULL_DOWN)

WIDTH =128
 
HEIGHT= 64
 
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)
 
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)

#Koordinaten des Spielers
plx = 0
ply = 10
#Größe des Spielers
plsizex = 16
plsizey = 16
    

#Code
while True:
   oled.fill(0)
   oled.fill_rect(plx, ply, plsizex, plsizey, 1)
   
   #Wenn der entsprechende Knopf gedrückt wird, werden die zugehörigen Koordinaten verändert.
   #Beachte, dass man sicherstellen muss, sich nicht aus dem Bildschirm herausbewegen zu können.
   
   #TODO
   
   #Bouns: Kannst du einen weiteren Gegenstand einbauen, der Kollisionen mit dem Spieler erkennen kann?
   
   oled.show()
 
 
 
 
