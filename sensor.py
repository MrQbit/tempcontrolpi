#!/usr/bin/python
import sys
import Adafruit_DHT

from RPLCD import CharLCD

lcd = CharLCD(cols=16, rows=2, pin_rs=23, pin_e=21, pins_data=[19, 15, 13, 11])


while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    lcd.cursor_pos = (0, 0)
    lcd.write_string("Temp: %d C" % temperature)
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Humidity: %d %%" % humidity)
    
