n = int(input("Digite um número: "))
cont = 0
dv = []
for i in range(n):
    if n%(i+1) == 0:
        cont+=1
        dv.append(i+1)
    else:
        cont
if cont == 2:
    print("O Número primo é divisivel por", dv)
else:
    print("O número não é primo pois ele é divisivel por", dv)