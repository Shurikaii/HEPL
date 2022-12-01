"""
File : ProjetChocapic_v1.3.MT.py
Author : Lorenz William ()
Date : 1/12/2022
Version : 1.3.MT (MultiThreaded)
"""



'''import enviroplus.gas as gas'''
import time, math, random
'''import RPi.GPIO as GPIO'''
from threading import Thread

# ---------- Functions (Threads) ---------- #

def ADCR():                                                                 
    U = 1.7
    while True:
        global TempTR
        t = time.time()
        t2 = 0
        '''U = gas.read_adc()'''
        U = U + random.uniform(-0.03,0.03) # used for tests
        TempTR = ((((math.log((3.3/U)-1))/3435)+(1/298.15))**-1)-273.15 
        while t2-t < 0.5:
            t2 = time.time()


def Print():                                               # Print temperature 1 time persec in terminal
    while True:
        time.sleep(1)
        print(f"{TempTR:.2f} °C")


def Alert():                                               # Turns on and off the LED depending on calculated temperature
    while True:
        t = time.time()
        t2 = 0
        if TempTR < 24:                                    # 2 Hz for too low temperature
            '''GPIO.output(4, GPIO.LOW)'''
            print(" / ") # used for tests
            time.sleep(0.25)
            '''GPIO.output(4, GPIO.HIGH)'''
            print(" \ ") # used for tests 
            time.sleep(0.25)
        elif TempTR > 28:                                  # 8 Hz for too high temperature
            while t-t2 < 0.5:
                t2 = time.time()
            '''GPIO.output(4, GPIO.LOW)'''
            print(" / ") # used for tests
            time.sleep(0.0625)
            '''GPIO.output(4, GPIO.HIGH)'''
            print(" \ ") # used for tests
            time.sleep(0.0625)
        else :
            '''GPIO.output(4, GPIO.HIGH)'''                 # Constently on for OK
            print("OK") # used for tests
            time.sleep(0.25)
            
# ----------- Setup ---------- #

'''gas.enable_adc()'''                                      # ADC input setup
'''gas.set_adc_gain(4.096)'''         

'''GPIO.setmode(GPIO.BCM)'''                                # LED output setup
'''GPIO.setup(4,GPIO.OUT)'''

# ---------- Multithreading ---------- #

threadlist = []                                          # Create an empty list of threads

threadlist.append(Thread(target=ADCR))                   # Add threads  to list
threadlist.append(Thread(target=Print))
threadlist.append(Thread(target=Alert))

for t in threadlist:                                     # Start multithreading
    t.start()
for t in threadlist:
    t.join()
    
