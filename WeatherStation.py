#Imports
from guizero import App, Text, TextBox, PushButton
from sense_emu import SenseHat

#global variable
sense = SenseHat()
valuelist = []

#Clearing SenseHat's led matrix
sense.clear()


#Functions
def led(ledcolor, value):
    
    #defining colors
    if ledcolor == 1:
        color = (0, 0, 255)
    elif ledcolor == 3:
        color = (255, 0, 0)
    elif ledcolor == 2:
        color = (0, 255, 0)
    
    #defining led columns for temperature pressure and humidity
    if value == 1:
        for x in range(2):
            for y in range(8):
                sense.set_pixel(x, y, color)
    elif value == 2:
        for x in range(3, 5):
            for y in range(8):
                sense.set_pixel(x, y, color)
    elif value == 3:
        for x in range(6, 8):
            for y in range(8):
                sense.set_pixel(x, y, color)
        


def read_sensehat(valuelist):
    valuelist = valuelist
    valuelist_sorted = []
    #temperature
    
    temp_now = f"{sense.temperature:5.1f}"
    pres_now = f"{sense.pressure:5.1f}"
    humi_now = f"{sense.humidity:5.1f}"
    valuelist.append(temp_now)
    valuelist.append(pres_now)
    valuelist.append(humi_now)
    for value in valuelist:
        try:
            value = float(value)
        except:
            value = None
        valuelist_sorted.append(value)
    
    temp_ap, pres_ap, humi_ap, temp_now, pres_now, humi_now = valuelist_sorted
    
    if temp_ap >= temp_now:
        led(2,1)
    elif temp_ap < temp_now:
        led(3,1)
    elif temp_ap == None:
        led(1,1)
    
    if pres_ap >= pres_now:
        led(2,2)
    elif pres_ap < pres_now:
        led(3,2)
    elif pres_ap == None:
        led(1,2)
        
    if humi_ap >= humi_now:
        led(2,3)
    elif humi_ap < humi_now:
        led(3,3)
    elif humi_ap == None:
        led(1,3)
    
    
#Application
class application:
    app = App(title = "SenseHat WeatherStation", layout = "auto")

    #Input boxes for alarm points
    widget_title = Text(app, text = "WeatherStation UI", size = 30, color = "black", height = "fill")
    empty_line1 = Text(app, text = "", height = "fill")
    message_temp = Text(app, text = "Please give alarm point for temperature on SenseHat (-30 - +105c)", height = "fill")
    temp_alarmpoint = TextBox(app, text = "23.0", height = "fill")
    message_pres = Text(app, text = "Please give alarm point for pressure on SenseHat (260 - 1260mbar)", height = "fill")
    pres_alarmpoint = TextBox(app, text = "160", height = "fill")
    message_humi = Text(app, text = "Please give alarm point for humidity on SenseHat (0 - 100%)", height = "fill")
    humi_alarmpoint = TextBox(app, text = "40", height = "fill")
    empty_line2 = Text(app, text = "", height = "fill")
    
    temp_ap = temp_alarmpoint.value
    pres_ap = pres_alarmpoint.value
    humi_ap = humi_alarmpoint.value
    valuelist.append(temp_ap)
    valuelist.append(pres_ap)
    valuelist.append(humi_ap)

    #Current values
    value_info_temp = Text(app, text = "Temperature now", height = "fill")
    value_temp = Text(app, text = f"{sense.temperature:5.1f}", size = 20, height = "fill")
    value_info_pres = Text(app, text = "Pressure now", height = "fill")
    value_pres = Text(app, text = f"{sense.pressure:5.1f}", size = 20, height = "fill")
    value_info_humi = Text(app, text = "Humidity now", height = "fill")
    value_humi = Text(app, text = f"{sense.humidity:5.1f}", size = 20, height = "fill")
    empty_line3 = Text(app, text = "", height = "fill")

    #Info for SenseHat's led matrix
    info_title = Text(app, text = "Info about SenseHat leds", size = 18, height = "fill")
    info = Text(app, text = """
    Led columns 0-1 are assigned to temperature.
    Led columns 3-4 are assigned to pressure.
    Led columns 6-7 are assigned to humidity.

    Green means value is at alarm point or under it
    and red means value is over alarm point.
    Blue means that there is no alarm point given.""", height = "fill")
    empty_line4 = Text(app, text = "", height = "fill")

    #Button for quitting program
    quit = PushButton(app, text = "Quit program", height = "fill", command = quit)
    
    app.repeat(5000, read_sensehat(valuelist))
    app.display()


    def quit():
        app.cancel(read_sensehat())
        app.disable()
        app.destroy()
    

if __name__ == '__main__':
    application()