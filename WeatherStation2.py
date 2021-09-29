#imports
from sense_emu import SenseHat
from guizero import App, Box, Text, TextBox, PushButton
from asyncio import create_task, run, sleep, wait

#variables
sense = SenseHat()

#clear SenseHat's led matrix
sense.clear()
        
        
#Functions
def main():
    run(read_sensehat())


async def led(color, value):
    if color == 0:
        rgb = (255, 0, 0)
        rgb2 = (255, 255, 255)
        i = 0
        while i < 5:
            if value == 0:
                for x in range(2):
                    for y in range(8):
                        if i % 2 == 0:
                            sense.set_pixel(x, y, rgb)
                        else:
                            sense.set_pixel(x, y, rgb2)
                await sleep(0.2)
            elif value == 1:
                for x in range(3, 5):
                    for y in range(8):
                        if i % 2 == 0:
                            sense.set_pixel(x, y, rgb)
                        else:
                            sense.set_pixel(x, y, rgb2)
                await sleep(0.2)
            elif value == 2:
                for x in range(6, 8):
                    for y in range(8):
                        if i % 2 == 0:
                            sense.set_pixel(x, y, rgb)
                        else:
                            sense.set_pixel(x, y, rgb2)
                await sleep(0.2)
            i += 1

    
    elif color == 1:
        rgb = (0, 255, 0)
    
        if value == 0:
            for x in range(2):
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


async def read_sensehat():
    temp_now.value = f"{sense.temperature:5.1f}"
    pres_now.value = f"{sense.pressure:5.1f}"
    humi_now.value = f"{sense.humidity:5.1f}"
    
    temperature_now = float(f"{sense.temperature:5.1f}")
    pressure_now = float(f"{sense.pressure:5.1f}")
    humidity_now = float(f"{sense.humidity:5.1f}")
    
    if temp_ap_input.value == "":
        task_temp = create_task(led(1,0))
        await sleep(1.2)
    else:
        if temperature_now < (float(temp_ap_input.value)):
            task_temp = create_task(led(0,0))
            await sleep(1.2)
        elif temperature_now >= (float(temp_ap_input.value)):
            task_temp = create_task(led(1,0))
            await sleep(1.2)
            
    if pres_ap_input.value == "":
        task_pres = create_task(led(1,1))
        await sleep(1.2)
    else:
        if pressure_now < (float(pres_ap_input.value)):
            task_pres = create_task(led(0,1))
            await sleep(1.2)
        elif pressure_now >= (float(pres_ap_input.value)):
            task_pres = create_task(led(1,1))
            await sleep(1.2)
    
    if humi_ap_input.value == "":
        task_humi = create_task(led(1,2))
        await sleep(1.2)
    else:
        if humidity_now < (float(humi_ap_input.value)):
            task_humi = create_task(led(0,2))
            await sleep(1.2)
        elif humidity_now >= (float(humi_ap_input.value)):
            task_humi = create_task(led(1,2))
            await sleep(1.2)
    

def quit():
    app.cancel(main)
    sense.clear()
    sense.show_message("Program stopped")
    
    app.disable()
    app.destroy()


#Main Program
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
     
app.repeat(2000, main)
app.display()
