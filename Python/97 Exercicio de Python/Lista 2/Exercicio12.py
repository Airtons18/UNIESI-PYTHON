sb = (5 * 220)
sind = (sb*3)/100
fgts = (sb*11)/100
inss = (sb*10)/100
if sb <= 900.00:
    ir = 0
elif sb <= 1500.00:
    perc = 5
    ir = (sb*5)/100
elif sb <= 2500.00:
    perc = 10
    ir = (sb*10)/100
else:
    perc = 20
    ir = (sb*20)/100
sl = sb - (ir+inss)
print("Salário Bruto                    :R$", sb)
print('(-) IR (', perc,'%)                    :R$', ir)
print('(-) INSS (', perc,'%)                  :R$', inss)
print('FGTS (11%)                       :R$', fgts)
print('Total de descontos               :R$', inss+ir)
print('Salário Líquido                  :R$', sl)