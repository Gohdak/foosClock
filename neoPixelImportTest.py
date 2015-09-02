#'s Clock
# -*- coding: utf-8 -*-
#Ref. NeoPixel library strandtest example
#see https://learn.adafruit.com/neopixels-on-raspberry-pi/software
#refer here about weather api: http://raspi.seesaa.net/article/415530289.html
#Author: Gohdak
#





import RPi.GPIO as GPIO

import time
from datetime import datetime
import math

import urllib2
import json

from neopixel import (
	begin,
	getPixelColor,
	getPixels,
	numPixels,
	setBrightness,
	setPixelColor,
	setPixelColorRGB,
	show,
	Color)





#config
LED_COUNT       = 56
LED_PIN         = 18
LED_FREQ_HZ     = 800000
LED_DMA         = 5
LED_BRIGHTNESS  = 255
LED_INVERT      = False




def main():
	#create NeoPixel object
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	#initialize the library
	strip.begin()

	print 'Press Ctrl-C to quit'

	while True:
		illuminateLED(strip, Color(255, 255, 255))





#define function illuminating LED
def illuminateLED(strip, color, wait_ms=50):
	if len(listPos) != strip.numPixels():
		return

	for i in range(strip.numPixels()):
		#case dark position
		if i * listPos[i - 1] == 0:
			strip.setPixelColor(i, Color(0, 0, 0))
			continue
		#case bright position
		else:
			strip.setPixelColor(i, color)

	strip.show()
	time.sleep(wait_ms/1000.0)





if __name__ == '__main__':
	main()
