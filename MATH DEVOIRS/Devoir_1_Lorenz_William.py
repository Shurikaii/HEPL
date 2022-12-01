
# File Devoir_1_Lorenz_William(1).py
# Code by Lorenz William (aka:シュリカイ)
# 14/10/2022


# ------------------------------ Lib & codecs ---------------------------------- #
import numpy as np
import matplotlib.pyplot as mplt

# ------------------------------ Functions ------------------------------------- #

def B(d):
    return ((4e-7 * 45)/(d))     # Simplified formula (deleted pi/pi)
    #return ((4e-7 * 45 * np.pi)/(np.pi * d))     # Original formula 
    
# ------------------------------ Variable d input ------------------------------ #

d = float(input("Distance from the cable (m) : "))
#d = 0.54     # for in-code value of d and to jump over this step to graphic

# ------------------------------ Output ---------------------------------------- #

''' Result of B(d) (in terminal) '''

print(f"B({d}m) = {(B(d)*1E+7):.2f} 1E-7 T")     # With units(T=Tesla), multiplied by 1E+7 and rounded to hundredths

''' Graphic ''' 

plt_title = "B(d)=\\frac{4.\pi.10^{-7}.45}{\pi.d} T"

abs = np.arange(0.001,10,1E-4)     # Min abs value = 0.01 (avoiding division by 0), Max abs value = 1, Calculation step = 1E-05
ord = B(abs)                      # Corresponding ordinate value (B(d))

mplt.plot(abs, ord)
mplt.xlim(-0.1,1.1)
mplt.ylim(-0.0001, 0.00175)
mplt.title("$%s$"%plt_title)

mplt.xlabel("d (m)")
mplt.ylabel("B(d) (T)")

mplt.ticklabel_format(axis='y',style='sci',scilimits=(0,0))
mplt.ticklabel_format(axis='x',style='sci',scilimits=(0,0))


mplt.grid(True)
mplt.show()
