np = int(input("Número de pessoas:> "))
cont = 0
idades = []
while cont < np:
    idd = int(input("Digite a Idade: "))
    idades.append(idd)
    cont+=1
midade = sum(idades)
midade = midade/cont
if midade <= 25:
    print("A Galera é Jovem !")
elif (midade <= 60):
    print("A Galera é Adulta !")
else:
    print("Os senhores são Idosos")