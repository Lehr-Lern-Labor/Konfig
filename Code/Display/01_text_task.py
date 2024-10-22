#Imports
from machine import Pin, I2C

from ssd1306 import SSD1306_I2C
 
import utime
 

#Variablen 
WIDTH =128
 
HEIGHT= 64
 
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)
 
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)


#Code
#Text an position 0,40 
oled.text("Lehr-Lern-Labor", 0, 40)

oled.show()
 
 
 
 
