l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))
slados = l1+l2
slados2 = l2+l3
slados3 = l1+l3
if slados > l3 and slados2 > l1 and slados3 > l2:
    print("É um Triângulo")
    if (l1 == l2) and (l1 == l3):
        print("Triângulo Equilátero: três lados iguais")
    elif (l1 == l2) or (l1 == l3) or (l2 == l3):
        print("Triângulo Isósceles: quaisquer dos lados iguais")
    else:
        print("Triângulo Escaleno: três lados diferentes")
else: 
    print("Não é um Triânulo!")