nnotas = int(input("Digite o número de notas que você irá digitar: "))
cont = 0
alln = []

while cont < nnotas:
    n = alln.append(float(input("Digite a nota: ")))
    cont += 1

m = sum(alln) / nnotas
print("A média é igual a ", '{:.2f}'.format(m))