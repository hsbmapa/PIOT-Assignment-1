from sense_hat import SenseHat
import random
import time
import sys
import game


sense = SenseHat()
sense.clear()

y = (255, 255, 0) #Yellow
b = (0, 0, 0) #Black

one = [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,y,y,b,b,b,
b,b,b,y,y,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b
]

two = [
b,b,b,b,b,b,b,b,
b,y,y,b,b,b,b,b,
b,y,y,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,y,y,b,
b,b,b,b,b,y,y,b,
b,b,b,b,b,b,b,b
]

three = [
b,b,b,b,b,b,b,b,
b,y,y,b,b,b,b,b,
b,y,y,b,b,b,b,b,
b,b,b,y,y,b,b,b,
b,b,b,y,y,b,b,b,
b,b,b,b,b,y,y,b,
b,b,b,b,b,y,y,b,
b,b,b,b,b,b,b,b
]

four = [
b,b,b,b,b,b,b,b,
b,y,y,b,b,y,y,b,
b,y,y,b,b,y,y,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,y,y,b,b,y,y,b,
b,y,y,b,b,y,y,b,
b,b,b,b,b,b,b,b
]

five = [
b,y,y,b,b,y,y,b,
b,y,y,b,b,y,y,b,
b,b,b,b,b,b,b,b,
b,b,b,y,y,b,b,b,
b,b,b,y,y,b,b,b,
b,b,b,b,b,b,b,b,
b,y,y,b,b,y,y,b,
b,y,y,b,b,y,y,b
]

six = [
b,y,y,b,b,y,y,b,
b,y,y,b,b,y,y,b,
b,b,b,b,b,b,b,b,
b,y,y,b,b,y,y,b,
b,y,y,b,b,y,y,b,
b,b,b,b,b,b,b,b,
b,y,y,b,b,y,y,b,
b,y,y,b,b,y,y,b
]



def roll():
    r = random.randint(1,6)
    if r == 1:
        sense.show_pixels(one)
    elif r == 2:
        sense.show_pixels(two)
    elif r == 3:
        sense.show_pixels(three)
    elif r == 4:
        sense.show_pixels(four)
    elif r == 5:
        sense.show_pixels(five)
    elif r == 6:
        sense.show_pixels(six)

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