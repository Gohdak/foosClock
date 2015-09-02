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
		#get hour and minute
		d = datetime.now()
		h1 = int(d.hour/10)
		h2 = d.hour%10
		m1 = int(d.minute/10)
		m2 = d.minute%10
		#convert each figures into binary position data
		listLightPos = []
		listLightPos = listFig(h1)
		listLightPos.extend(listFig(h2))
		listLightPos.extend([1, 1, 1, 1])	#colon
		listLightPos.extend(listFig(m1))
		listLightPos.extend(listFig(m2))

		#get weather info
		weatherType = weather()

		#convert weatherType into Color
		weatherColor(weatherType)

		#illuminate LED
		illuminateLED(strip, Color(255, 255, 255), listLightPos)





#define function which converts figure into binary position list
#LED position id for each digits
#  10* 11* 12*
#   9*     13*
#   8*  7*  6*
#   1*      5*
#   2*  3*  4*
def listFig(figure):
#				1  2  3  4  5  6  7  8  9 10 11 12 13
	if figure == 0:
		#case 0
		return [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
	elif figure == 1:
		#case 1
		return [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1]
	elif figure == 2:
		#case 2
		return [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1]
	elif figure == 3:
		#case 3
		return [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
	elif figure == 4:
		#case 4
		return [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]
	elif figure == 5:
		#case 5
		return [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
	elif figure == 6:
		#case 6
		return [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
	elif figure == 7:
		#case 7
		return [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
	elif figure == 8:
		#case 8
		return [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	elif figure == 9:
		#case 9
		return [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]





#define function getting weather info as 'telop'
def weather():
	try:
		city = '2620400';	#Uji
		json_url = 'http://weather.livedoor.com/forecast/webservice/json/v1' #API URL

		r = urllib2.urlopen('%s?city=%s' % (json_url, city) )
    	obj = json.loads( unicode(r.read()) )

    	forecasts = obj['forecasts']

    	cast = forecasts[0]

		return cast['telop']
	finally:
		r.close()

	return





#define function converting weather into color
def weatherColor(type):
	if type == u'曇時々晴':
		return Color(255, 255, 255)
	elif type == u'曇時々雨':
		return Color(255, 255, 255)
	elif type == u'曇時々雪':
		return Color(255, 255, 255)
	elif type == u'晴時々曇':
		return Color(255, 255, 255)
	elif type == u'晴時々雨':
		return Color(255, 255, 255)
	elif type == u'雨時々曇':
		return Color(255, 255, 255)
	elif type == u'晴のち曇':
		return Color(255, 255, 255)
	elif type == u'晴のち雨':
		return Color(255, 255, 255)
	elif type == u'曇のち晴':
		return Color(255, 255, 255)
	elif type == u'曇のち雨':
		return Color(255, 255, 255)
	elif type == u'雨のち晴':
		return Color(255, 255, 255)
	elif type == u'雨のち曇':
		return Color(255, 255, 255)
	elif type == u'雪のち曇':
		return Color(255, 255, 255)
	elif type == u'曇のち雪':
		return Color(255, 255, 255)
	elif type == u'雨':
		return Color(255, 255, 255)
	elif type == u'晴れ':
		return Color(255, 255, 255)
	elif type == u'曇り':
		return Color(255, 255, 255)
	elif type == u'雪':
		return Color(255, 255, 255)
	else:
		return Color(255, 255, 255)





#define function illuminating LED
def illuminateLED(strip, color, listPos, wait_ms=50):
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





#execute
try:
	if __name__ == '__main__':
		main()
except KeyboardInterrupt:
	pass
GPIO.cleanup()
