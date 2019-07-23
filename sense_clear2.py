#! /usr/bin/python3

from sense_hat import SenseHat
sense = SenseHat()
#this script will clear any LEDs in the "on" state

print("clearing LEDs")

sense.clear()
