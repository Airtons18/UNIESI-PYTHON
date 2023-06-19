def pn(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1

z = False
while z != True:
    x = int(input("Digite um número inteiro: "))
    p = pn(x)
    print(p)
    r = input("Deseja parar? S/N --> ")
    if r == "s":
        z = True
    else:
        pass




