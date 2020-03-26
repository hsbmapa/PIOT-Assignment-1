from sense_hat import SenseHat
from time import sleep
import sys
import json

sense = SenseHat()

# Define colours
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Reading the json file for temperature limits
with open('config.json', 'r') as f:
  data = json.load(f)

# Get temperature from Sense Hat
temp = sense.get_temperature()

# Round off the temperature to 1 decimal place
temp = round(temp, 1)

#Create message by converting the value to a string
message = str(temp)

if data['comfortable_min'] <= temp <= data['comfortable_max']:
  txt = green
elif temp <= data['cold_max']:
  txt = blue
else :
  txt = red

while True:
	try:
		sense.show_message(str(temp), scroll_speed = 0.2, text_colour = txt)
		sleep(10)
	except KeyboardInterrupt:
		sense.clear()
		sys.exit()
