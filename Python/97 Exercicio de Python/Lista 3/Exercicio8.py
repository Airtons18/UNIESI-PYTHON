L = []
for x in range(1, 6, 1):
    n = float(input("Digite um número: "))
    L.append(n)
print("A soma é: ", sum(L))
s = sum(L)
l = len(L)
m = s/l
print("A Média é: ", m)