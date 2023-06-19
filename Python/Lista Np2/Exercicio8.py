def circ(r):
    pi = 3.141592
    a = pi * r**2
    return a

def quad(l):
    a = l**2
    return a

def retan(b, h):
    a = b*h
    return a

def triang(b, h):
    a = (b*h)/2
    return a

z = False
while z != True:
    p = 0
    resp = int(input("Calcular area de?\n 1-Circulo\n 2-Quadrado\n 3-Retângulo\n 4-Triângulo\n 5-Sair\n Opcão:  "))
    if resp == 1:
        r = float(input("Digite o Raio: "))
        p = circ(r)
        print(p)
    elif resp == 2:
        l = float(input("Digite o valor do L: "))
        p = quad(l)
        print(p)
    elif resp == 3:
        b = float(input("Digite o valor da Base: "))
        h = float(input("Digite o valor da Altura: "))
        p = retan(b, h)
        print(p)
    elif resp == 4:
        b = float(input("Digite o valor da Base: "))
        h = float(input("Digite o valor da Altura: "))
        p = triang(b, h)
        print(p)
    else:
        z = True


