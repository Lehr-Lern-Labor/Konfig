#Imports
from machine import Pin, I2C

from ssd1306 import SSD1306_I2C
 
 
#Variablen
WIDTH =128
 
HEIGHT= 64
 
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)
 
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)

#Koordinaten des Vierecks
rectx = 0
recty = 10
#Größe des Vierecks
sizex = 32
sizey = 32

#Code
while True:
   oled.fill(0)
   oled.fill_rect(rectx, recty, sizex, sizey, 1)
   
   #Das viereck bewegt sich zwischen dem rechten und linken Bildschirmrand
   #TODO
   
   oled.show()
 
 
 
 
