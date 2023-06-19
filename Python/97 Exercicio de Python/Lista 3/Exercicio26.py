neleitores = int(input("Quantos eleitores são?: ->"))
candidados = [1, 2, 3]
cont = 0
x = 0
y = 0
z = 0
while cont < neleitores:
    v = int(input("Para votar digite 1 = João / 2 = Tadeu / 3 = Maria --> "))
    cont+=1
    if v == 1:
        x = x+1
    elif v == 2:
        y = y+1
    elif v == 3:
        z = z+1
print("O Canditado 1 recebeu", x)
print("O Canditado 2 recebeu", y)
print("O Canditado 3 recebeu", z)
if x > y and x > z:
    print("O Candidato 1 ganhou com", x, "votos")
elif y > x and y > z:
    print("O Candidato 2 ganhou com", y, "votos")
else:
    print("O Candidato 3 ganhou com", z, "votos")