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

a = "Hello, World!"


szamlalo = 1 
for x in a:
    if szamlalo % 2 == 0:
        print(a[szamlalo-1], end="")
    szamlalo = szamlalo + 1