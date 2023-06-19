L = []
nvezes = int(input("Quantas vezes vai digitar o número: "))
x = 0
vn = 0
while x < nvezes:
    while vn < 0:
        n = int(input("Digite um número: "))
        if (n >= 0) and (n <= 1000):
            vn = 1
        else:
            print("Numero invalido!")
    x+= 1
    L.append(n)
print("O Maior numero digitado foi: ", max(L))
print("O Menor valor digitador foi: ", min(L))
print("A Soma dos valores foi: ", sum(L))
