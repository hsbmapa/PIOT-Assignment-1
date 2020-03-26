from sense_hat import SenseHat
from time import sleep
import sys

sense = SenseHat()

g = (0, 255, 0) #Green
b = (0, 0, 0) #Black
f = (139, 69, 19) #Brown
w = (255, 255, 255) #White
y = (128, 128, 128) #Gray


creeper_happy = [
   g, g, g, g, g, g, g, g,
   g, g, g, g, g, g, g, g,
   g, b, b, g, g, b, b, g,
   g, b, b, g, g, b, b, g,
   g, g, g, g, g, g, g, g,
   g, b, b, g, g, b, b, g,
   g, g, g, b, b, g, g, g,
   g, g, g, g, g, g, g, g
]

creeper_frown = [
   g, g, g, g, g, g, g, g,
   g, g, g, g, g, g, g, g,
   g, b, b, g, g, b, b, g,
   g, b, b, g, g, b, b, g,
   g, g, g, g, g, g, g, g,
   g, g, g, b, b, g, g, g,
   g, g, b, g, g, b, g, g,
   g, b, g, g, g, g, b, g
]

cow_face = [
   f, f, f, f, f, f, f, f,
   f, f, f, f, f, f, f, f,
   w, w, f, f, f, f, w, w,
   b, w, f, f, f, f, b, w,
   f, f, f, f, f, f, f, f,
   f, f, w, w, w, w, f, f,
   f, w, b, y, y, b, w, f,
   f, w, y, y, y, y, w, f
]

while True:
   try:
      sense.set_pixels(creeper_happy)
      sleep(3)
      sense.set_pixels(creeper_frown)
      sleep(3)
      sense.set_pixels(cow_face)
      sleep(3)
   except KeyboardInterrupt:
      sense.clear()
      sys.exit()
