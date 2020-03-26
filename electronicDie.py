from sense_hat import SenseHat
import time
import random
import sys

sense = SenseHat()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
magenta = (255,0,255)
aqua = (0,255,255)
yellow = (255,255,0)

def roll():
	r = random.randint(1,6)
	if r == 1:
		sense.show_letter("1", text_colour=red)
	elif r == 2:
		sense.show_letter("2", text_colour=blue)
	elif r == 3:
		sense.show_letter("3", text_colour=green)
	elif r == 4:
		sense.show_letter("4", text_colour=magenta)
	elif r == 5:
		sense.show_letter("5", text_colour=aqua)
	elif r == 6:
		sense.show_letter("6", text_colour=yellow)

while True:
	try:
		acceleration = sense.get_accelerometer_raw()
		x = acceleration['x']
		y = acceleration['y']
		z = acceleration['z']

		x = abs(x)
		y = abs(y)
		z = abs(z)

		if x > 1.5 or y > 1.5 or z > 1.5:
				roll()
				time.sleep(2)
				sense.clear()
				time.sleep(1)

	except KeyboardInterrupt:
		sense.clear()
		sys.exit()
