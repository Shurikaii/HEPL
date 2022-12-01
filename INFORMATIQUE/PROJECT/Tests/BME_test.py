import bme280, time, ST7735
from PIL import Image, ImageDraw, ImageFont
import fonts

bme = bme280.BME280()
bme.setup()
time.sleep(0.1)
'''while True:
 t = bme.get_temperature()
 p = bme.get_pressure()
 h = bme.get_humidity()
 a = bme.get_altitude(qnh=999)
 l= bme.get_luminosity
 print(f"Temperature :\n{t:.2f} °C\n")
 print(f"Pression :\n{p:.2f} hPa\n")
 print(f"Humidité :\n{h:.2f} %\n")
 print(f"Altitude:\n{a:.2f} m")'''

while True :
    disp.setup