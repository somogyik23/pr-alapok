"""
szam1 = int(input("Kérek egy egész számot:"))
szam2 = int(input("Kérek egy másik egész számot:"))
if szam1 < szam2:
    print("szam1 nagyobb mint szam2")
if szam2 > szam1:
    print("szam2 nagyobb mint szam1")
if szam1 == szam2:
    print("szam1 megegyezik szam2-vel")
"""
"""
szam1 = int(input("Kérek egy egész számot:"))
szam2 = int(input("Kérek egy másik egész számot:"))
if szam1 < szam2:
    print("szam1 nagyobb mint szam2")
elif szam2 > szam1:
    print("szam2 nagyobb mint szam1")
elif szam1 == szam2:
    print("szam1 megegyezik szam2-vel")
"""
"""    
szam1 = int(input("Kérek egy egész számot:"))
szam2 = int(input("Kérek egy másik egész számot:"))
if szam1 < szam2:
    print("szam1 nagyobb mint szam2")
elif szam2 > szam1:
    print("szam2 nagyobb mint szam1")
else szam1 == szam2:
    print("szam1 megegyezik szam2-vel")
"""  

"""
x = None
print(x)
print(type(x))

if x:
    print("Do you think None is True?")
elif x is False:
    print("Do you think None is False?")
else:
    print("None is not True, or False, None is just None...")
"""
"""
jegy = input("Kérek egy osztályzatot:")
if jegy == "1":
    print("elégtelen")
elif jegy == "2":
    print("elégséges")
elif jegy == "3":
    print("közepes")
elif jegy == "4":
    print("jó")
elif jegy == "5":
    print("jeles")
else:
    print("Érvvénytelen osztályzatot adtál!")
"""
"""
#Bekérek egy pozitív egész számot és irassuk ki hogy páros vagy páratlan.

szam = int(input("Kérek egy pozitív egész számot"))
szam = % 2 
if szam == 0:
    print("a szám páros")
else szam == 1:
    print("a szám páratlan")
"""
"""
import random

gondolt_szám = random.randint(1,6)
print('Súgok:', gondolt_szám)
tipp = input('Gondoltam egy számra. Tippeld meg! ')
"""

import random

gondolt_szám = random.randint(1,1000)
print (gondolt_szám)
if gondolt_szám % 2 == 0 and gondolt_szám <= 500:
    print("Jó")
else:
    print("Rosz")



