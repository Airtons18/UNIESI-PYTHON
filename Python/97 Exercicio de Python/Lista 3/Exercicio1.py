x = 0
while x < 1:
    n = float(input("Digite uma nota: "))
    if (n >= 0) and (n <= 10):
        x = 1
    else:
        print("Nota Invalida")
print("Nota Valida")