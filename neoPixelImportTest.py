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
