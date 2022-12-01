# File : Devoir_4_Lorenz_William.py
# Code by Lorenz William (aka: Shurikaï)
# 14/10/2022


# ------------------------------ Lib & codecs ---------------------------------- #

from scipy.misc import derivative
import numpy as np
import matplotlib.pyplot as mplt
import sympy 

# ------------------------------ Functions ------------------------------------- #

def F(X):
    return np.sin(X**4+9)

def f(x):
    return derivative(F, x, dx=1e-6)

# ------------------------------ Variables ------------------------------------- #
Fx = []
fx = []
x =[]
#x0 = float(input("Studied point :"))

for i in range (-5000,5000):
    Fx.append(F(i/100))
    fx.append(f(i/100))
    x.append(i/100)

#print(f(x0))

mplt.plot(x, Fx)
#mplt.plot(x,fx)


mplt.xlim(-5,5)
#mplt.ylim(-100,100)


mplt.grid(True)
mplt.show()