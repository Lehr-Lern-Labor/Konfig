###Imports###
from machine import Pin
from time import sleep



###Variablen###
led = Pin("LED",Pin.OUT)
long = 1.5
short = 0.5
char_wait = 1.5
word_wait = 2 

morse_dict = {
    "A": "sl",
    "B": "lsss",
    "C": "lsls",
    "D": "lss",
    "E": "s",
    "F": "ssls",
    "G": "lls",
    "H": "ssss",
    "I": "ss",
    "J": "slll",
    "K": "lsl",
    "L": "slss",
    "M": "ll",
    "N": "ls",
    "O": "lll",
    "P": "slls",
    "Q": "llsl",
    "R": "sls",
    "S": "sss",
    "T": "l",
    "U": "ssl",
    "V": "sssl",
    "W": "sll",
    "X": "lssl",
    "Y": "lsll",
    "Z": "llss",
    " ": "P",
}



###Code###
#Verwendet das gegebene Dictionary, um einen Satz aus Großbuchstaben in Morsecode umzuwandeln.
#Dieser Satz in Morsecode, wird dann für die Weiterverwendung zurückgegeben.
#Hinweis: Mit morse_dict["A"] wird auf den Eintrag von "A" zugegriffen
#Hinweis: Mit return kann eine Methode einen Wert zurückgeben
#Bonus: Überlege dir, wie man mit mehr Eingaben als nur Großbuchstaben umgehen könnte.
def translate_to_morse(sentence):
    morse = ""
    #TODO
    return morse

#Bekommt einen Satz aus Großbuchstaben und bildet diese als Morsecode ab, indem die LED in den
#entsprechenden Längen aufleuchtet.
def show_morse(sentence):
    morse = translate_to_morse(sentence)
    #TODO
