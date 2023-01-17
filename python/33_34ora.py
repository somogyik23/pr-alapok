#1.1 feladat
"""
szo = str(input("Kérek egy szót: "))
print(szo.upper())
"""
#1.2 feladat
"""
lista = ["Kutya", "Macska", "Egér", "Mókus"]
masik_lista = [szo.upper() for szo in lista]
print('Eredeti: ', lista)
print('Nagybetűs: ', masik_lista)
"""
#1.3 feladat
"""
lista = ["Kutya", "Macska", "Egér", "Mókus", "Erd"]
masik_lista = [szo.upper() for szo in lista if len(szo) > 3]
print('Eredeti: ', lista)
print('Nagybetűs: ', masik_lista)
"""
#1.4 feladat
"""
lista = ['egyszer', 'volt', 'hol', 'nem', 'volt']

mas_lista = [szo.swapcase() for szo in lista]

print('Eredeti:', lista)
print('Másik:', mas_lista)
"""

#2.1 feladat
"""
megadott_tartomany = list(range(-3, 5))

ertek = [2 * x - 3 for x in megadott_tartomany]

print('Értelemzési tartomány:', megadott_tartomany)
print('Érték készlet:', ertek)
"""

#2.2 feladat
"""
megadott_tartomany = list(range(-3, 5))

ertek = [2 * x - 3 for x in megadott_tartomany if x >= 0]

print('Értelemzési tartomány:', megadott_tartomany)
print('Érték készlet:', ertek)
"""
#-----------------------------------------------------------------------------
#1.1 feladat
"""
paletta = ['kék', 'piros', 'sárga', 'lila', 'zöld']

szin = input('írjon be egy színt: ')

print('A', szin, 'már' if szin in paletta else 'még nem', 'szerepel a listában: ')
"""

#1.2 feladat

paletta = ['fekete', 'fekete', 'piros', 'sárga', 'sárga', 'fekete', 'sárga']

szin = input('írjon be egy színt: ')

if szin in paletta:
    print('A', szin, len([arnyalat for arnyalat in paletta if arnyalat == szin]), '-szor szerepel a listában:', ', '.join(paletta))
else:
    print('A megadott szín nem szerepel a listában')