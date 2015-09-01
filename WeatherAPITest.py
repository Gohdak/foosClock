#Weather API Test
# -*- coding: utf-8 -*-
#ref http://raspi.seesaa.net/article/415530289.html
#Author Gohdak

import urllib2
import json

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
