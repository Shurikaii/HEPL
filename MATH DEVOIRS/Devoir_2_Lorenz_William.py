# File : Devoir_2_Lorenz_William.py
# Code by Lorenz William (aka : Shurikaï)
# 10/11/2022

# ------------------------------ Lib & codecs ---------------------------------- #

import math as mt 

# ------------------------------ Functions ------------------------------------- #

def F(x):
    return((mt.tan(72*x))/x)

# ------------------------------ Variables ------------------------------------- #

list = []
xlist = []
x = -0.1
niter = int(input('Number of iteration (recomended : 7) : \n'))
n = 0

# ------------------------------ Output ---------------------------------------- #

while n != niter :
    list.append(f'{F(x):.5f}')
    xlist.append(f'{x:.5f}')
    x = x/4
    n = n + 1
    
n = 0
x = -x*4
list.append('|||| 0/0 ||||')          # Left-Right limits seperators
xlist.append('|||| 0 ||||')

while n != niter :
    list.append(f'{F(x):.5f}')
    xlist.append(f'{x:.5f}')
    x = x*4
    n = n + 1
 
 
print (f'Left and right limits :'
       f'\n\n- x value : \n    {xlist}' 
       f'\n\n- F(x) value : \n    {list}' 
       f'\n\n- Symbolic lim(x -> 0) F(x) value : \n    {F(1e-300):.2f} ')









# Code could be shorter but would be less aesthetic and fun ^^ (no notable perf impact !) #