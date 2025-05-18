from machine import Pin
from neopixel import NeoPixel
import time
import random

from machine import Pin, I2C
import mcp4728

i2c = I2C(0, scl=Pin(3), sda=Pin(46), freq=400000)
print(i2c.scan())

dac1=mcp4728.MCP4728(i2c,0x60)
dac1.a.vref=0
dac1.a.value=4095

pin = Pin(45, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, 1)   # create NeoPixel driver on GPIO0 for 8 pixels
while True:
    np[0] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    np.write()	# write data to all pixels
    time.sleep_ms(1000)
    