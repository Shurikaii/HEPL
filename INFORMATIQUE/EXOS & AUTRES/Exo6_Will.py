import cmath
i = int(input("Nombre de nombres :"))
X = i+1
liste = []
while(i != 0):
    a = int(input(f"Nombre {X-i} :"))
    liste.append(a)
    i = i-1
liste.sort()
print(liste)