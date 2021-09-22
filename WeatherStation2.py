#imports
from sense_emu import SenseHat
from guizero import App, Box, Text, TextBox, PushButton

#variables
sense = SenseHat()

#clear SenseHat's led matrix
sense.clear()

app = App(title = "SenseHat WeatherStation", layout = "grid")

upper_box = Box(app, grid = [0,0,1,3])
emptyline1 = Text(upper_box, text = "")
label = Text(upper_box, text = "**** SenseHat WeatherStation ****", size = 24)
emptyline1 = Text(upper_box, text = "")

middle_box = Box(app, grid = [0,3,1,11], layout = "grid")

temp_box = Box(middle_box, grid = [0,0,12,3], border=True, layout = "grid")
temp_box_label = Text(temp_box, text = "TEMPERATURE", grid = [0,0])
temp_now = Text(temp_box, text = f"now: {sense.temperature:5.1f}", grid =[0,1], align = "left")
temp_ap_text = Text(temp_box, text = "Alarmpoint: ", grid = [0,2], align = "left")
temp_ap_input = TextBox(temp_box, grid = [1,2,1,1], align = "left")

emptyline2 = Text(middle_box, text = "", grid = [0,3])

pres_box = Box(middle_box, grid = [0,4,12,3], border=True, layout = "grid")
pres_box_label = Text(pres_box, text = "AIRPRESSURE", grid = [0,0])
pres_now = Text(pres_box, text = f"now: {sense.pressure:5.1f}", grid =[0,1], align = "left")
pres_ap_text = Text(pres_box, text = "Alarmpoint: ", grid = [0,2], align = "left")
pres_ap_input = TextBox(pres_box, grid = [1,2,1,1], align = "left")

emptyline3 = Text(middle_box, text = "", grid = [0,7])

humi_box = Box(middle_box, grid = [0,8,12,3], border=True, layout = "grid")
humi_box_label = Text(humi_box, text = "HUMIDITY", grid = [0,0])
humi_now = Text(humi_box, text = f"now: {sense.humidity:5.1f}", grid =[0,1], align = "left")
humi_ap_text = Text(humi_box, text = "Alarmpoint: ", grid = [0,2], align = "left")
humi_ap_input = TextBox(humi_box, grid = [1,2,1,1], align = "left")

emptyline4 = Text(middle_box, text = "", grid = [0,7])

lower_box = Box(app, grid = [0,16,1,2])
emptyline5 = Text(lower_box, text = "", grid = [0,7])
quit = PushButton(lower_box, text = "Quit program", width = "fill", grid = [0,1], command = quit)
     
app.repeat(5000, read_sensehat)
app.display()


def quit():
    app.cancel(read_sensehat)
    app.disable()
    app.destroy()
        
        
def led(color, value):
    if color == red:
        rgb = (255, 0, 0)
        rgb2 = (255, 255, 255)
    elif color == green:
        rgb = (0, 255, 0)
        rgb2 = (0, 255, 0)
    
    if value == temp:
        for x in range(2):
            for y in range(8):
                sense.set_pixel(x, y, rgb)
        
    elif value == pres:
        for x in range(3, 5):
            for y in range(8):
                sense.set_pixel(x, y, rgb)
    elif value == humi:
        for x in range(6, 8):
            for y in range(8):
                sense.set_pixel(x, y, rgb)
        

def read_sensehat():
    temp_now = float(f"{sense.temperature:5.1f}")
    pres_now = float(f"{sense.pressure:5.1f}")
    humi_now = float(f"{sense.humidity:5.1f}")
    
    if temp_ap_input.value == "":
        led(green, temp)
    else:
        if temp_now < (float(temp_ap_input.value)):
            led(red,temp)
        elif temp_nov >= (float(temp_ap_input.value)):
            led(green, temp)
    
    if pres_ap_input.value == "":
        led(green, pres)
    else:
        if pres_now < (float(pres_ap_input.value)):
            led(red, pres)
        elif pres_now >= (float(pres_ap_input.value)):
            led(green, pres)
    
    if humi_ap_input.value == "":
        led(green, humi)
    else:
        if humi_now < (float(humi_ap_input.value)):
            led(red, humi)
        elif humi_now >= (float(humi_ap_input.value)):
            led(green, humi)
        led(2,2)
    if pres_ap < pres_now:
        led(3,2)
    elif pres_ap == None:
        led(1,2)
        
    if humi_ap >= humi_now:
        led(2,3)
    elif humi_ap < humi_now:
        led(3,3)
    elif humi_ap == None:
        led(1,3)
