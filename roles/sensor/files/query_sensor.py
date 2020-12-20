#!/usr/bin/env python
from __future__ import print_function
import Adafruit_DHT, getopt, sys
import time

SENSOR_CODE = Adafruit_DHT.AM2302
GPIO_PIN = 17

def query_sensors(pin, sensor):
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            return "%f,%f" % (humidity, temperature)
        else:
            raise Exception("Could not read from %i sensor on pin %i" % (sensor, pin))

if __name__=='__main__':
	pin = GPIO_PIN
	sensor = SENSOR_CODE
	argumentList = sys.argv[1:]
	try:
		optlist, args = getopt.getopt(argumentList, "p:s:")
	except getopt.GetoptError as err:
		sys.exit(1)
	for o, a in optlist:
		if o == "-p":
			pin = a
		elif o == "-s":
			sensor = a
	try:
		print("%f,%s" % (time.time(), query_sensors(pin, sensor)))
	except Exception as e:
		print(e, file=sys.stderr)


