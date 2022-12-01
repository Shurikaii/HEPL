import time
import ST7735
from PIL import Image, ImageDraw, ImageFont
from fonts.ttf import RobotoMedium as UserFont
from bme280 import BME280
from smbus import SMBus
from ltr559 import LTR559
bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

ltr559 = LTR559()


disp = ST7735.ST7735(port=0, cs=1, dc=9, backlight=12,rotation=270, spi_speed_hz=10000000)
disp.begin()
WIDTH = disp.width
HEIGHT = disp.height
def lcdDisplay(message, back_colour, text_colour):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0,0))
    draw = ImageDraw.Draw(img)
    font_size = 25
    font = ImageFont.truetype(UserFont, font_size)
    size_x, size_y = draw.textsize(message, font)
    x = (WIDTH - size_x) / 2
    y = (HEIGHT / 2) - (size_y / 2)
    draw.rectangle((0, 0, 160, 80), back_colour)
    draw.text((x, y), message, font=font,fill=text_colour)
    disp.display(img)
def enableLcd():
    disp.set_backlight(100)
def disableLcd():
    disp.set_backlight(0)
while True:
    lux = ltr559.get_lux()
    prox = ltr559.get_proximity()
    

    enableLcd()
#affiche "Hello, world" en rouge avec un fond noir surl'écran LCD
    time.sleep(1.0)
    if prox> 10 :
        temperature = bme280.get_temperature()
        pressure = bme280.get_pressure()
        humidity = bme280.get_humidity()
          
        
        
        lcdDisplay("Temperature: \n{:05.2f} *C".format(temperature), (0, 0, 0), (255, 0, 0))
        time.sleep(2.0)
        lcdDisplay("Pressure:\n{:05.2f} hPa".format(pressure), (0, 0, 0), (255, 0, 0))
        time.sleep(2.0)
        lcdDisplay("Humidity: \n{:05.2f}".format(humidity), (0, 0, 0), (255, 0, 0))
        time.sleep(2.0)
        #lcdDisplay("Proximity : \n {:05.2f} ".format(prox), (0, 0, 0), (255, 0, 0))
        
        
    

    if prox<1000 :
        lcdDisplay("Come near \n       me", (0, 0, 0), (105, 150, 0))
        
    