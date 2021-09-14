"""Sense HAT kortin käsittelyesimerkki

    Tässä ohjelmassa luetaan Sense HAT kortilta lämpötila
    ja näytetään se konsolilla.
    Ohjelma lopetetaan, kun painetaan ohjainsauvaa
    Sense HAT kortilla.
"""

# Sense HAT rajapinnan haku
#from sense_hat import SenseHat # fyysinen kortti
from sense_emu import SenseHat # emulaattori

from time import sleep # odotusfunktio sleep

def main():
    """Testipääohjelma

    """
    
    # luodaan Sense HAT olio
    sense = SenseHat()
    
    # pääohjelmasilmukka
    while True:
        """rivi = input("Lopetetaan enterillä")
        if len(rivi) == 0:
            break"""
        
        # lopetetaan, kun painetaan joystickia
        joy = sense.stick.get_events() # luetaan tapahtumat
        if joy: # lopetetaan, kun koskettu joystickiin
            break
        
        # tulostetaan lämpötila
        #print(f"{sense.get_temperature():4.1f}")
        print(f"{sense.temperature:4.1f}", end="\r")
        
        sleep(0.5) # odotetaan puoli sekuntia
        
    print("Lopetetaan!") ## ohjelman lopuksi
    
if __name__ == '__main__':
    main()