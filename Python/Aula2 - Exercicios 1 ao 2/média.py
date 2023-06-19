x = 0
while (x <= 1):
    nome = input("Nome: ")
    np1 = float(input("Nota Np1: "))
    np2 = float(input("Nota Np2: "))
    media = ((np1+np2)/2)
    print(nome, "sua média é ", media)
    print("                                             @Author: Airton Aparecido dos Santos Neto")
    if (media < 7):
        print("REPROVADO")
    else:
        print("Aprovado!")
    x = int(input("1 - Continuar | 2 - Cancelar |  --> "))