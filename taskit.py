"""Rinnakkaisuuden toteutus taskeilla

    Käytetään edelleen SenseHHAT emulaattoria.
    Luetaan saman aikaisesti input-tietoa näppäimistöltä
    ja käsitellään SenseHATttia.
"""
from sense_emu import SenseHat

from asyncio import run, create_task, wait, sleep

from aioconsole import ainput # konsolien hallinta taskeissa
# tarvitaan suorittaa komentotulkissa 'pip3 install aioconsole'

global stop # muuttuja stop globaaliksi

async def main():
    global stop
    
    stop = False
    
    # luodaan taskit readhat
    print("eka")
    task1 = create_task(readHat())
    task2 = create_task(konsoli())
    print("toka")
    
    # odotellaan, kunnes taski on lopetettu
    await wait({task1})
    task2.cancel() # pakotetaan task2 lopettamaan
    print("kola")
    await wait({task2})
    print("nela")

async def konsoli():
    global stop
    
    """Konsolikäyttöliittymä
    """
    try:
        while True:
            rivi = await ainput("")
            if len(rivi) == 0 or stop:
                stop = True
                break
    except:
        print("keskeytys")
        stop = True

async def readHat():
    global stop
    
    # Sense HAT olion luonti
    sense = SenseHat()
    
    # pääohjelmasilmukka
    while True:
        print(f"{sense.temperature:5.2f}", end="\r") # luetaan ja tulostetaan lämpötila
        
        if sense.stick.get_events() or stop: # onko koskettu joystickiin?
            stop = True
            break # lopetetaan silmukka
        
        await sleep(1) # odotellaan yksi sekunti ennen jatkamista
    
if __name__ == '__main__':
    run(main())
    
