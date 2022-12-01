from enviroplus import gas
import bme280, time, csv, math
import RPi.GPIO as GPIO
from datetime import datetime


bme = bme280.BME280()
bme.setup()
time.sleep(0.1)
gas.enable_adc()
gas.set_adc_gain(4.096)
date = datetime.today()

while True:
    data = open(f"/home/pi/Desktop/B14/Projet Tom & WIll/ADCR_Data_{date}.csv","a")
    Mwriter = csv.writer(data, delimiter = ";")    
    TempBME = bme.get_temperature()
    U = gas.read_adc()
    TempTR = ((((math.log((3.3/U)-1))/3435)+(1/298.15))**-1)-273.15
    print(U,"\n", TempBME, "\n", TempTR)
    Mwriter.writerow([TempBME,U, TempTR])
    
    data.close()
    time.sleep(2)
    
