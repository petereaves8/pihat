#!/usr/bin/env python

#this script will define colors for a scrolling message on the Pi HAT
from sense_hat import SenseHat
sense = SenseHat()

#use RGB values to define colors
yellow = (155, 155, 0)
blue = (0, 155, 155)

speed = 0.08

message = raw_input()

sense.show_message(message, speed, text_colour=yellow, back_colour=blue)

sense.clear()
