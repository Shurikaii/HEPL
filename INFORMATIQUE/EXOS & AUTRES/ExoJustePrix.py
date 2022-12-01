import random
i = 0
prix = random.randrange(10000, 40000)
print(prix)
x = 0
while x != prix:
    i = i + 1
    x = float(input("Entrez une réponse (10000-40000 $) :"))
    if x < prix:
        print("C'est plus !")
    elif x > prix:
        print("C'est moins !")
    elif x > 40000 or x < 10000 :
        print("N'oubliez pas, l'estimation doit être comprise entre 10000 et 40000 $")
    
if i == 1 :
    print("Whaouh vous avez trouvez du premier coup ! Incroyable !")
else :
    print(f"Félicitations ça ne vous aura pris que {i} essais pour trouver LE JUSTE PRIX")