sc = float(input("Salário: R$"))
if sc <= 280.00:
    per = 20 
    aumento = (sc*20)/100
elif sc <= 700.00:
    per = 15
    aumento = (sc*15)/100
elif sc <= 1500.00:
    per = 10
    aumento = (sc*10)/100
elif sc > 1500.00:
    per = 5
    aumento = (sc*5)/100
print("===================================")
print("Salário Antigo: R$", sc)
print("Percentual de Aumento: ", per)
print("Valor do Aumento: ", aumento)
print("Novo Salário: ", sc+aumento)