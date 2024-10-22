###Imports###
from machine import Pin, PWM
from time import sleep



###Variablen###
#pwm verweist auf den Pin an dem eine LED angeschlossen ist, z.B. 17
pwm = PWM(Pin("""TODO"""))
max_helligkeit = 65025
min_helligkeit = 0
frequenz = 1000



###Code###
#Bonus: Versuche unterschiedliche Frequenzen aufzustellen und zu beobachten was passiert.
pwm.freq(frequenz)

def aus():
    pwm.duty_u16(min_helligkeit)
def viertelHell():
    pwm.duty_u16(max_helligkeit//4)
def halbHell():
    pwm.duty_u16(max_helligkeit//2)
def an():
    pwm.duty_u16(max_helligkeit)

while True:
    #Lässt die LED zunehmend heller werden
    for helligkeit in range(max_helligkeit):
        #TODO
        sleep(0.0001)
    #Lässt die LED zunehmend dunkler werden
    for helligkeit in range(max_helligkeit, min_helligkeit, -1):
        #TODO
        sleep(0.0001)
        