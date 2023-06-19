import math
saque = input("Valor para sacar: R$")
n100 = 0
n50 = 0
n10 = 0
n5 = 0
n1 = 0
if len(saque) == 3:
    c = saque[0:1]
    c = int(c)
    d = saque[1:2]
    d = int(d)
    u = saque[2:3]
    u = int(u)
if d > 4:
    n50 = 1
    d = d-5
if u > 5:
    n5 = 1
    u = u-5
n100 = c
n10 = d
n1 = u
print("Notas de 100: ", n100)
print("Notas de 50: ", n50)
print("Notas de 10: ", n10)
print("Notas de 5: ", n5)
print("Notas de 1: ", n1)