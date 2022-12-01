import time
from bme280 import BME280
from smbus import SMBus
from ltr559 import LTR559
bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

ltr559 = LTR559()

while True:
    lux = ltr559.get_lux()
    prox = ltr559.get_proximity()
    time.sleep(1.0) 

    if prox> 1000 :
        temperature = bme280.get_temperature()
        pressure = bme280.get_pressure()
        humidity = bme280.get_humidity()
        print("Temperature: {:05.2f} *C, Pressure: {:05.2f} hPa, Relative humidity: {:05.2f}".format(temperature,pressure, humidity))
        time.sleep(1.0) 
    else :
        print("Nothing near")
    
    
    
    