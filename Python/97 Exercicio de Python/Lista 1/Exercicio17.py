import math
mq = float(input("Tamanho em Metros Quadrados: "))
litros = mq/6
x = 0
qtbalde = 0
qtgalao = 0
if (litros <= 10.8):
    ntinta = litros/3.6
    while x < 1:
        qtgalao+= 1
        if qtgalao > ntinta:
            x = 1
elif (litros <= 18):
    ntinta = litros/18
    while x < 1:
        qtbalde+= 1
        if qtbalde > ntinta:
            x = 1
elif (litros > 18):
    ntinta = litros/18
    n1tinta = litros/3.6
    while x < 1:
        qtbalde+= 1
        if qtbalde > ntinta:
            qtfinalb = qtbalde
            x2 = 0
            while x2 < 1:
                qtgalao+= 1
                if qtgalao > n1tinta:
                    qtfinalg = qtgalao
                    soma = qtfinalb + qtfinalg
                    soma2 = ntinta + n1tinta 
                    if (soma) >= (soma2):
                        x2 = 1
                        x = 1
print("=========================================================")
print("=========================================================")
print("Baldes Necessario: ", qtbalde)
print("Galões Necessario: ", qtgalao)
print("Litros de Tinta: ", '{:.2f}'.format(litros))
"""
porcentagemlitros = (litros*10)/100
litros = round(litros+round(porcentagemlitros, 2), 2)
print("Margem de 10% ", round(porcentagemlitros, 2), "Total: ", litros)
"""
totalb = qtbalde*80
print("Preço Galão de 3.6L Unidade", qtgalao, "Total= R$", qtgalao*25.00)
totalg = qtgalao*25
print("Preço Balde de 18L Unidade", qtbalde, "Total= R$", qtbalde*80.00)
balde = int(litros/18)
teste = int(litros/18)*18
litrosint = round(litros - teste, 2)/3.6
litrosint = math.ceil(litrosint)
print("Baldes", balde, "Galões", litrosint, "Total R$", (balde*80)+(litrosint*25))
totaldeg = (balde*80)+(litrosint*25)
L = [totalb, totalg, totaldeg]
print("Menor preço entre as três propostas é: R$", min(L))
dezporcem = (min(L)*10)/100
dezporcem = (min(L)+dezporcem)
print("Menor preço com 10%: R$", dezporcem)
print("=========================================================")
print("=========================================================")