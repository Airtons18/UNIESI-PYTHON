L = []
nvezes = int(input("Quantas vezes vai digitar o número: "))
nvezes+=1
for x in range(1, nvezes, 1):
    n = int(input("Digite um número: "))
    L.append(n)
print("O Maior numero digitado foi: ", max(L))
print("O Menor valor digitador foi: ", min(L))
print("A Soma dos valores foi: ", sum(L))