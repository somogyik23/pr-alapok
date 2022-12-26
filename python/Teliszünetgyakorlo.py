#Elágazások/Véletlenszámok/1.Feladat
"""
import random

random_szam = random.randint(1,3)
print(random_szam)

szam = int(input('Kérek egy számot 1-3 között! '))

if random_szam == szam:
    print("A szám egyezik")

elif random_szam < szam:
    print("Az ön választott száma nagyobb mint a random szám")

else:
    random_szam > szam
    print("Az ön választott száma kisebb mint a random szám")
"""
#------------------------------------------------------------------------
#Elágazások/Véletlenszámok/2.Feladat
"""
import random

random_szam = random.randint(1,2)

szam = int(input("Fej vagy Írás? Nyomj egy 1 est ha fej 2 ha írás "))

if szam == random_szam:
    print("Siker Talált :) ")

else:
    szam != random_szam
    print("Ez most nem talált :( ") 
"""
#-------------------------------------------------------------------------
#Ciklusok/While ciklus/1.feladat
"""
szam = 2
while szam <= 10:
    print(szam)
    szam = szam + 2
"""
#-------------------------------------------------------------------------   
#Ciklusok/While ciklus/2.feladat
"""
szam = 10
while szam >= 1:
    print(szam)
    szam = szam - 1
"""
#-------------------------------------------------------------------------
#Lísták/Listák létrehozása/1.1feladat
"""
keresztnevek = []

while True:
    nev = input("Írj be keresztneveket: ")
    if not nev:
        break
    keresztnevek.append(nev)

print('A keresztnév:', keresztnevek)
"""
#-------------------------------------------------------------------------
#Lísták/Listák létrehozása/1.2feladat
"""
keresztnevek = []

while True:
    nevek = input("Írj be keresztneveket: ")
    if not nevek:
        break
    keresztnevek.append(nevek)
    if len(keresztnevek) == 3:
        print("Nem írhatsz be több nevet")
        break
"""