import time, ST7735, bme280
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
time.sleep(0.1)
while True:
    t = bme.get_temperature()
    p = bme.get_pressure()
    h = bme.get_humidity()
    a = bme.get_altitude(qnh=999)
    l = bme.get_
    enableLcd()
    lcdDisplay(f"Température : {t}°C", (0, 0, 0), (255, 0, 0))
    time.sleep(1.0)
