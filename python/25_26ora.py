
lista = ["alma","banán","cseresznye"]
print(lista)

#--------------------------------------------------------------

lista = ["alma","banán","cseresznye","alma","banán"]
print(lista)

#--------------------------------------------------------------

lista = ["alma","banán","cseresznye"]
print(len(list))

#--------------------------------------------------------------

lista1 = ["alma","banán","cseresznye"]
lista2 = [1, 5, 7, 9, 3]
lista3 = [True, False, False]

#--------------------------------------------------------------

lista5 = ["alma", "banán","cseresznye"]
print(type(lista5))

#--------------------------------------------------------------

lista = (("alma", "banán","cseresznye"))
print(lista)

#--------------------------------------------------------------

lista = (("alma", "banán","cseresznye"))
print(lista[1])

#--------------------------------------------------------------

lista = (("alma", "banán","cseresznye"))
print(lista[-1])

#--------------------------------------------------------------

lista = ["alma", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
print([2:5])

#-------------------------------------------------------------

lista = ["alma", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
print([1:6])

#-------------------------------------------------------------

lista = ["alma", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
print([:4])

#-------------------------------------------------------------

lista = ["alma", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
print([2:])

#-------------------------------------------------------------

lista = ["alma", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
print([-4:-1])

#-------------------------------------------------------------

lista = ["alma", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
if "banán-1" in lista
print("Igen a banán-1 szerepel  a lsitában")

#-------------------------------------------------------------

lista = ["alma", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
if "banán-1" not in lista
print("Igen a banán-1 nem szerepel  a lsitában")

#-------------------------------------------------------------

lista = ["alma", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
lista([1:2]) = ["Körte", "szilva"]
print(lista)

#-------------------------------------------------------------

lista = ["alma", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
lista([1:3]) = ["Körte"]
print(lista)

#-------------------------------------------------------------

lista = ["alma-0", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
lista.insert(2, "körte")
print(lista)

#-------------------------------------------------------------

lista = ["alma", "banán", "cseresznye"]
lista.append("körte")
print(lista)