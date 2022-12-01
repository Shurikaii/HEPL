import math

def max_2(x,y):
    if x >= y :
        return x
    elif x < y :
        return y

def max_4(w,x,y,z):
    m1 = max_2(w,x)
    m2 = max_2(y,z)
    return max_2(m1,m2)
    
    
i = float(input("First number : \n"))
j = float(input("Second number : \n"))
k = float(input("Third number : \n"))
l = float(input("Fourth number : \n"))

print(f"Biggest number : \n {max_4(i,j,k,l)}")