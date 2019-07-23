#!/usr/bin/env python

from sense_hat import SenseHat
import time
import random
sense = SenseHat()

r1 = random.randint(0, 255)
r2 = random.randint(0, 255)
r3 = random.randint(0, 255)

print("The random numbers are ", r1, r2, r3, " this time.")

sense.show_letter("H", (r1, r2, r3))
time.sleep(1)
sense.show_letter("i", (r2, r3, r1))
time.sleep(1)
sense.show_letter("!", (r3, r1, r2))
time.sleep(1)
sense.clear()

print("Operation Complete!")
