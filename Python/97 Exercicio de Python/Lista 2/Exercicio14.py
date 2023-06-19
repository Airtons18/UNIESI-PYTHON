n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
m = (n1+n2)/2
if m <= 4:
    print("Média:", m)
    print("Conceito: E")
    print("REPROVADO")
elif m <= 6:
    print("Média:", m)
    print("Conceito: D")
    print('REPROVADO')
elif m <= 7.5:
    print("Média:", m)
    print("Conceito: C")
    print('APROVADO')
elif m <= 9:
    print("Média:", m)
    print("Conceito: B")
    print('APROVADO')
else:
    print("Média:", m)
    print("Conceito: A")
    print('APROVADO')