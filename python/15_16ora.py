"""
print("Hello")

print('Hello')
"""
# ----------------------------------------------------------
"""
a = "Hello"

print(a)
"""
# ----------------------------------------------------------
'''
a = """Lorem ipsum dolor sit amet,

consectetur adipiscing elit,

sed do eiusmod tempor incididunt

ut labore et dolore magna aliqua."""

print(a)
'''
# ----------------------------------------------------------
"""
a = "Hello, World!"

print(a[1])

print(a[4])
"""
# ----------------------------------------------------------
"""
for x in "banana":

  print(x, end= ' ', sep="-")
"""
# ----------------------------------------------------------
"""
a = "Hello, World!"

print(len(a))
print(a[len(a)-1])
print("az utolso index: ",len(a)-1)
"""
# ----------------------------------------------------------
"""
a = "Hello, World!"


szamlalo = 1 
for x in a:
    if szamlalo % 2 == 0:
        print(a[szamlalo-1], end="")
    szamlalo = szamlalo + 1
"""
# ----------------------------------------------------------
"""
txt = "The best things in life are free!"
print("free" in txt) # True
"""
# ----------------------------------------------------------
"""
b = "Hello, World!"
print(b[2:5]) # llo
"""
# ----------------------------------------------------------
"""
b = "Hello, World!"
print(b[:5]) # Hello
"""
# ----------------------------------------------------------
"""
b = "Hello, World!"
print(b[2:]) # llo, World!                                                   
"""
# ----------------------------------------------------------
"""
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())
"""
# ----------------------------------------------------------
"""
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"                  
"""
# ----------------------------------------------------------
"""
a = " Hello, World! "
print(a.replace("J", "H")) # returns "Hello, World!"
"""
# ----------------------------------------------------------

a = " Hello, World! "
print(a.split(",")) # returns ['Hello, World!']
lista = a.split(",")
print(lista[3])
b = "44;341;223;333;54544"
lista1 = b.split(";")
print(lista1[3])        