import time, ST7735, bme280
from ltr559 import LTR559
from PIL import Image, ImageDraw, ImageFont
from fonts.ttf import RobotoMedium as UserFont


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
    
bme = bme280.BME280()
bme.setup()
ltr = LTR559()

time.sleep(0.1)
while True:
    prox = ltr.get_proximity()
    image = Image.open("/home/pi/Desktop/B14/Projet Tom & WIll/logo.png")
    image = image.resize(WIDTH,HEIGHT)
    if prox > 10 :
        t = bme.get_temperature()
        p = bme.get_pressure()
        h = bme.get_humidity()
        a = bme.get_altitude(qnh=999)
        lux = ltr.get_lux()
    
        enableLcd()
        lcdDisplay("",(0, 0, 0), (255, 255, 255))
        disp.display(image)
        time.sleep(2.0)
        lcdDisplay(f"Luminosity :\n{lux:.0f} lx", (0, 0, 0), (255, 255, 255))
        time.sleep(1.5)   
             
        lcdDisplay(f"Température :\n{t:.1f} °C", (0, 0, 0), (255, 0, 0))
        time.sleep(1.5)

        lcdDisplay(f"Pressure :\n{p:.0f} hPa", (0, 0, 0), (0, 255, 0))
        time.sleep(1.5)
        
        lcdDisplay(f"Humidity :\n{h:.1f} %", (0, 0, 0), (0, 0, 255))
        time.sleep(1.5)
        
        lcdDisplay(f"Altitude :\n{a:.1f} m", (0, 0, 0), (255, 75, 255))
        time.sleep(1.5)
    
        disableLcd()
    #else : 
        #lcdDisplay(f"Approchez\nvotre main",(0, 0, 0), (255, 0, 0))
    
