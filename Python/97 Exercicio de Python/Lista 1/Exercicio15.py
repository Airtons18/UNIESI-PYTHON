vh = float(input("Valor da hora: R$"))
ht = float(input("Horas Trabalhadas: "))
sb = vh*ht*30
ir = (sb*11)/100
inss = (sb*8)/100
sind = (sb*5)/100
sl = sb - (ir+inss+sind)
print("Salário Bruto: R$", '{:.2f}'.format(sb))
print("IR: R$-", '{:.2f}'.format(ir))
print("INSS: R$-", '{:.2f}'.format(inss))
print("Sindicato: R$-", '{:.2f}'.format(sind))
print("Salário Líquido: R$=", '{:.2f}'.format(sl))