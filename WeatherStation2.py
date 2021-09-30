#imports
from sense_emu import SenseHat   #Emulated SenseHat
from guizero import App, Box, Text, TextBox, PushButton   #Guizero for Graphical User Interface
from asyncio import create_task, run, sleep, wait #Asyncio for asynchronous programming/tasks
from azure.iot.device import IoTHubDeviceClient, Message   #For interacting with Azure IoTHub
from datetime import datetime   #For creating a timestamp
from time import time   #For checking duration between transmissions
import json   #For working with JSON format
import auth   #File containing keys for accessing Azure - inside .gitignore

#Variables
sense = SenseHat()
primary_connection_string = auth.primary_connection_string
connected_device = IoTHubDeviceClient.create_from_connection_string(primary_connection_string)

#For connecting to Azure IotHub
connected_device.connect()

#For defining time_then variable for the first time
global time_now, time_then
time_then = time()
time_now = time()

#clear SenseHat's led matrix
sense.clear()
        
        
#Functions
#For starting asynchronous function read_sensehat
def main():
    global time_now, time_then
    time_now = time()
    if (time_now - time_then) > 60:   #comparison to make transmissions send if duration
        time_then = time_now          #between now and then is more than 60 seconds
        run(read_sensehat(1))
    else:
        run(read_sensehat(0))


#Asynchronous function for blinking color red and white leds if the value goes under the alarm
#point. First two led columns reserved for temperature, second for pressure and third for
#humidity plus empty column between each. Green light means that value is over the given
#alarmpoint. Used tasks to have asynchronous led blinking.
async def led(color, value):
    if color == 0:   #color 0 means red/white
        rgb = (255, 0, 0)
        rgb2 = (255, 255, 255)
        i = 0
        while i < 7:
            if value == 0:   #value 0 means temperature
                for x in range(2):
                    for y in range(8):
                        if i % 2 == 0:
                            sense.set_pixel(x, y, rgb)
                        else:
                            sense.set_pixel(x, y, rgb2)
                await sleep(0.2)
            elif value == 1:   #value 1 means pressure
                for x in range(3, 5):
                    for y in range(8):
                        if i % 2 == 0:
                            sense.set_pixel(x, y, rgb)
                        else:
                            sense.set_pixel(x, y, rgb2)
                await sleep(0.2)
            elif value == 2:   #value 2 means humidity
                for x in range(6, 8):
                    for y in range(8):
                        if i % 2 == 0:
                            sense.set_pixel(x, y, rgb)
                        else:
                            sense.set_pixel(x, y, rgb2)
                await sleep(0.2)
            i += 1

    
    elif color == 1:   #color 1 means green
        rgb = (0, 255, 0)
    
        if value == 0:
            for x in range(2):   #using here and above two for-loops to build x and y coordinates
                for y in range(8):
                    sense.set_pixel(x, y, rgb)        
        elif value == 1:
            for x in range(3, 5):
                for y in range(8):
                    sense.set_pixel(x, y, rgb)
        elif value == 2:
            for x in range(6, 8):
                for y in range(8):
                    sense.set_pixel(x, y, rgb)


#For sending information to IoTHub of Azure
async def send_transmission(temp, pres, humi):
    if temp_ap_input.value != "":
        temp_ap = float(temp_ap_input.value)
    else:
        temp_ap = None
    if pres_ap_input.value != "":
        pres_ap = float(pres_ap_input.value)
    else:
        pres_ap = None
    if humi_ap_input.value != "":
        humi_ap = float(humi_ap_input.value)
    else:
        humi_ap = None
    
    timestamp = datetime.now()
    timestamp = timestamp.strftime("%d.%m.%Y - %H:%M:%S")
    
    msg = json.dumps(\
        {
         'DeviceID': auth.deviceid,
         'Temperature': temp,
         'Temperature_alarmpoint': temp_ap,
         'Pressure': pres,
         'Pressure_alarmpoint': pres_ap,
         'Humidity': humi,
         'Humidity_alarmpoint': humi_ap,
         'Time_stamp': timestamp
        }
        )
    message = Message(msg)
    connected_device.send_message(message)


#Reading SenseHat for values and writing them on the GUI. Running asynchronous led function
#based on comparison of value versus alarmpoint. Running asynchronous send_transmission function
async def read_sensehat(time):
    temp_now.value = f"now: {sense.temperature:5.1f}"
    pres_now.value = f"now: {sense.pressure:5.1f}"
    humi_now.value = f"now: {sense.humidity:5.1f}"
    
    temperature_now = float(f"{sense.temperature:5.1f}")
    pressure_now = float(f"{sense.pressure:5.1f}")
    humidity_now = float(f"{sense.humidity:5.1f}")
    
    if time == 1:
        task_message = create_task(send_transmission(temperature_now, pressure_now, humidity_now))
        await task_message
    else:
        pass
    
    if temp_ap_input.value == "":
        task_temp = create_task(led(1,0))
        await sleep(0.5)
    else:
        if temperature_now < (float(temp_ap_input.value)):
            task_temp = create_task(led(0,0))
            await sleep(0.5)
        elif temperature_now >= (float(temp_ap_input.value)):
            task_temp = create_task(led(1,0))
            await sleep(0.5)
            
    if pres_ap_input.value == "":
        task_pres = create_task(led(1,1))
        await sleep(0.5)
    else:
        if pressure_now < (float(pres_ap_input.value)):
            task_pres = create_task(led(0,1))
            await sleep(0.7)
        elif pressure_now >= (float(pres_ap_input.value)):
            task_pres = create_task(led(1,1))
            await sleep(0.5)
    
    if humi_ap_input.value == "":
        task_humi = create_task(led(1,2))
        await sleep(0.5)
    else:
        if humidity_now < (float(humi_ap_input.value)):
            task_humi = create_task(led(0,2))
            await sleep(0.9)
        elif humidity_now >= (float(humi_ap_input.value)):
            task_humi = create_task(led(1,2))
            await sleep(0.5)
    
    if sense.stick.get_events():
        app.cancel(main)
        sense.clear()
        sense.show_message("Program stopped by stick event")
    
        app.disable()
        app.destroy()
        connected_device.disconnect()


#For quitting program and show message of program stop with sensehat leds
def quit():
    app.cancel(main)
    sense.clear()
    sense.show_message("Program stopped by Quit button")
    
    app.disable()
    app.destroy()
    connected_device.disconnect()


#Main GUIZERO Program - Eventloop
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
     
app.repeat(2000, main)   #Had to use main function because was not able to run asynchronous 
app.display()            #function inside app.repeat.
