n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1+n2)/2
if (media >= 6):
    print("APROVADO")
elif (media >=4) and (media < 6):
    print("EXAME")
else:
    print("REPROVADO")
print("Sua média é de", media)