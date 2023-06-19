kgpeixe = float(input("Peso de peixes: "))
if (kgpeixe > 50.0):
    excesso = (kgpeixe - 50)
    multa = excesso*4.00
print("======================================")
print("Peso peixe: ", kgpeixe, "Kg")
print("Excedeu: ", excesso, "Kg")
print("Multa: R$", multa)
print("======================================")