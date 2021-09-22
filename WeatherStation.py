#Imports
from guizero import App, Text, TextBox, Box, PushButton
from sense_emu import SenseHat
from time import sleep


#global variable
sense = SenseHat()

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
        


def read_sensehat():
    #temperature
    value_temp = f"{sense.temperature:5.1f}" #value_temp.VALUE removed
    
    try:
        message_temp = float(message_temp.value)
        value_temp = float(value_temp)
    except:
        led(1,1)
    else:
        if message_temp >= value_temp:
            led(2,1)
        else:
            led(3,1)
    
    #pressure
    value_pres = f"{sense.pressure:5.1f}"
    
    try:
        message_pres = float(message_pres.value)
        value_pres = float(value_pres)
    except:
        led(1,2)
    else:
        if message_pres >= value_pres:
            led(2,2)
        else:
            led(3,2)
    
    #humidity
    value_humi = f"{sense.humidity:5.1f}"
    
    try:
        message_humi = float(message_humi.value)
        value_humi = float(value_humi)
    except:
        led(1,3)
    else:
        if message_humi >= value_humi:
            led(2,3)
        else:
            led(3,3) 


#Application
class application:
    app = App(title = "SenseHat WeatherStation")

    #Input boxes for alarm points
    widget_title = Text(app, text = "WeatherStation UI", size = 30, color = "black")
    empty_line1 = Text(app, text = "")
    message_temp = Text(app, text = "Please give alarm point for temperature on SenseHat (-30 - +105c)")
    temp_alarmpoint = TextBox(app)
    message_pres = Text(app, text = "Please give alarm point for pressure on SenseHat (260 - 1260mbar)")
    pres_alarmpoint = TextBox(app)
    message_humi = Text(app, text = "Please give alarm point for humidity on SenseHat (0 - 100%)")
    humi_alarmpoint = TextBox(app)
    empty_line2 = Text(app, text = "")

    #Current values
    value_info_temp = Text(app, text = "Temperature now")
    value_temp = Text(app, text = f"{sense.temperature:5.1f}", size = 20)
    value_info_pres = Text(app, text = "Pressure now")
    value_pres = Text(app, text = f"{sense.pressure:5.1f}", size = 20)
    value_info_humi = Text(app, text = "Humidity now")
    value_humi = Text(app, text = f"{sense.humidity:5.1f}", size = 20)
    empty_line3 = Text(app, text = "")

    #Info for SenseHat's led matrix
    info_title = Text(app, text = "Info about SenseHat leds", size = 18)
    info = Text(app, text = """
    Led columns 0-1 are assigned to temperature.
    Led columns 3-4 are assigned to pressure.
    Led columns 6-7 are assigned to humidity.

    Green means value is at alarm point or under it
    and red means value is alarm point.
    Blue means that there is no alarm point given.""")
    empty_line4 = Text(app, text = "")

    #Button for quitting program
    quit = PushButton(app, text = "Quit program", command = quit)
    
    app.repeat(1000, read_sensehat)
    app.display()


    def quit():
        app.disable()
        app.destroy()
    

if __name__ == '__main__':
    application()