#NeoPixel import test
# -*- coding: utf-8 -*-
#Ref. NeoPixel library strandtest example
#see https://learn.adafruit.com/neopixels-on-raspberry-pi/software
#Author: Gohdak
#





#import RPi.GPIO as GPIO
import time


from neopixel import *
#from neopixel import (
#	begin,
#	getPixelColor,
#	getPixels,
#	numPixels,
#	setBrightness,
#	setPixelColor,
#	setPixelColorRGB,
#	show,
#	Color)





#config
LED_COUNT       = 1
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
		illuminateLED(strip, Color(0, 255, 0))
		time.sleep(1)
		illuminateLED(strip, Color(255, 0, 0))
		time.sleep(1)
		illuminateLED(strip, Color(0, 0, 255))
		time.sleep(1)





#define function illuminating LED
def illuminateLED(strip, color, wait_ms=50):

	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)

	strip.show()
	time.sleep(wait_ms/1000.0)





if __name__ == '__main__':
	main()
