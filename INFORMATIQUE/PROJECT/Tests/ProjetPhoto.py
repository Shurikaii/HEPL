from enviroplus import gas
import time

gas.enable_adc()
gas.set_adc_gain(4.096)



while True:
    U = gas.read_adc()
    print(U)
    
    if U >= 2.6:
        print("Nuit")
    elif U >= 2 and U < 2.6:
        print("Matin/Soirée")
    else :
        print("Jour")
    time.sleep(3)