import time
from ltr559 import LTR559
ltr559 = LTR559()

while True:
    lux = ltr559.get_lux()
    prox = ltr559.get_proximity()
    print("Light: {:05.02f} Lux, Proximity: {:05.02f}".format(lux, prox))
    time.sleep(1.0)