#!/usr/bin/env python

from sense_hat import SenseHat
import time
import random
sense = SenseHat()

counter = 0


while (counter != 100):
	rc1 = random.randint(0,7)
	rc2 = random.randint(0,7)

	r1 = random.randint(0,255)
	r2 = random.randint(0,255)
	r3 = random.randint(0,255)

	sense.set_pixel(rc1,rc2 , (r1, r2, r3))
	time.sleep(.2)
	sense.clear()
	counter = counter + 1
