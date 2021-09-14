import guizero

from sense_emu import SenseHat

class application:
    def __init__(self):
        self.sensehat = SenseHat()
        
        self.app = guizero.App("Eka gui-sovellus")
        
        self.box = guizero.Box(self.app, layout="grid", height="fill", width="fill")
        
        self.text = guizero.Text(self.box, text="Example", grid=[0, 0])
        
        self.text_temperature = guizero.Text(self.box, text=f"{self.sensehat.temperature:5.2f}", grid=[1, 0])
        
        self.lopeta = guizero.PushButton(self.box, text="Lopeta", grid=[0,3], command=self.lopeta_onclick)
        
        self.app.repeat(1000, self.read_sensehat)
        
        self.app.display()
        
    def read_sensehat(self):
        self.text_temperature.value = f"{self.sensehat.temperature:5.2f}"
        
        if self.sensehat.stick.get_events():
            self.app.cancel(self.read_sensehat)
            self.app.disable()
            self.app.destroy()
            
    def lopeta_onclick(self):        
        self.app.cancel(self.read_sensehat)
        self.app.disable()
        self.app.destroy()
        
if __name__ == '__main__':
    application() # kutsutaan muodostinta
