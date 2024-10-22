###Imports###
from machine import Pin, PWM, ADC
from time import sleep



###Variablen###
#Pin für die LED
pwm = PWM(Pin("""TODO"""))
#Pin für das Potenziometer
adc = ADC(Pin("""TODO""")) 
frequenz = 1000



###Code###
pwm.freq(frequenz)

def aus():
    pwm.duty_u16(0)

#Liest den Wert des Potenziometers aus und speichert diesen in Helligkeit.
#Damit kann die Helligkeit der LED eingestellt werden.
while True:
    helligkeit = adc.read_u16()
    print(helligkeit)
    sleep(1)
    #TODO

        