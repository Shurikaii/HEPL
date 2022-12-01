import cmath
import math
#variables
a=int(input("Entrez valeur de a :"))
b=int(input("Entrez valeur de  b :"))
c=int(input("Entrez valeur de  c :"))
#calculations
delta = b ** 2 - (4 * a * c)
print(f"delta = {delta}")

if delta < 0:
    print("Aucun résultats dans les réels => passage aux complexes")
    Xi1 = ( - b + cmath.sqrt(delta)) / (2 * a)
    Xi2 = ( - b - cmath.sqrt(delta)) / (2 * a)
    print(f"x1 = {Xi1:.2f} et x2 = {Xi2:.2f}")
  
elif delta is 0:
    x1 = ( - b + math.sqrt(delta)) / (2 * a)
    print(f"x = {x1:.2f}")
else:
    x1 = ( - b + math.sqrt(delta)) / (2 * a)
    x2 = ( - b - math.sqrt(delta)) / (2 * a)
    print(f"x1 = {x1:.2f} et x2 = {x2:.2f}")
