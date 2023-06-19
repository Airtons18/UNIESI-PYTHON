import math

mq = float(input("Metros Quadrados: "))
litros = mq/3
if (litros < 18):
    print("Numero de latas: 1")
    print("Litros: ", '{:.2f}'.format(litros))
    print("Preço total: R$ 80.00")
else:
        nlatas = (litros/18)
        nlatas = math.ceil(nlatas)
        print("Numero de latas: ", nlatas)
        print("Litros: ", '{:.2f}'.format(litros))
        print("Preço total: R$", nlatas*80)