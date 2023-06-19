a = input("Telefonou para a vítima?") 
b = input("Esteve no local do crime?") 
c = input("Mora perto da vítima?") 
d = input("Devia para a vítima?") 
e = input("Já trabalhou com a vítima?")
s = 0
if a == "sim":
    s = s+1
if b == "sim":
    s = s+1
if c == "sim":
    s = s+1
if d == "sim":
    s = s+1
if e == 'sim':
    s = s+1
if s <= 1:
    print("Inocente")
elif s <= 2:
    print("Suspeito")
elif s <= 4:
    print("Cúmplice")
else:
    print("Assasino")