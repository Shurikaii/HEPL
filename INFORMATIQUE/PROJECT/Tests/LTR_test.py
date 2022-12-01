import ltr559, time

ltr = ltr559.LTR559()
time.sleep(0.5)

while True: 
    prox = ltr.get_proximity()
    lux = ltr.get_lux()

    print(f"Proxi : {prox}")
    print(f"Light : {lux}")