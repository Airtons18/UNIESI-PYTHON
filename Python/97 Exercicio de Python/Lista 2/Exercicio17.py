ano = int(input("Ano: "))
vdv4 = ano%4
vdv100 = ano%100
vdv400 = ano%400
if vdv4 == 0 and vdv100 != 0:
    print("O Ano", ano, "é Bissexto")
elif vdv4 != 0 and vdv400 != 0:
    print("O Ano", ano, "não é Bissexto!")
elif vdv4 != 0 or vdv400 == 0:
    print("O Ano", ano, "é Bissexto!")