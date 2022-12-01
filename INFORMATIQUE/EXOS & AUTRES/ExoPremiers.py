import cmath

def P(x) :
    n = 2
    if x < 2 :
        return False
    elif x == 2 :
        return True
    r = x % n
    while n != x:
        if r == 0:
            return False
        else :
            n = n+1
    if r != 0:
        return True

while True :
    y = int(input("Number to test : "))
    print(f"Is {y} a prime number : {P(y)}")