n = int(input("Digite um número: "))
dv = []
cont = 0

for i in range(n + 1):
    if i%2 == 1 and i != 2:
        dv.append(i)
        cont += 1
    else:
        cont += 1
print("Números primos: ", dv)
print("Número de divisões", cont)