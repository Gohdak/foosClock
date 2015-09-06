#Weather API Test
# -*- coding: utf-8 -*-
#ref http://raspi.seesaa.net/article/415530289.html
#Author Gohdak
#
#Requirement
#pip install simple json

import urllib2
import json





#main
def main():
<<<<<<< HEAD
	telop = weather()
	print telop
=======
	string = weather()
	print string
>>>>>>> cfa22e2ad2f05af644d96202849d8e9941d683e2



#define function getting weather info as 'telop'
def weather():
	try:
		#city = '2620400'	#Uji
		city = '130010'		#Tokyo
		json_url = 'http://weather.livedoor.com/forecast/webservice/json/v1' #API URL

		r = urllib2.urlopen('%s?city=%s' % (json_url, city) )
<<<<<<< HEAD
    		obj = json.load( unicode(r.read()) )
=======
    	obj = json.load( unicode(r.read()) )
>>>>>>> cfa22e2ad2f05af644d96202849d8e9941d683e2

    		forecasts = obj['forecasts']

    		cast = forecasts[0]

		return cast['telop']
	finally:
		r.close()

	return





if __name__ == '__main__':
	main()
