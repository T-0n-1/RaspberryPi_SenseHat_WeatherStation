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
          