RE = int(input("Digite Receita Estadual: "))
nome = input("Digite o nome: ")
repsal = 0
while (repsal <= 0):
    salario = float(input("Salario: R$"))
    if (salario >= 998.00):
        repsal = 1
    else:
        print("Salário minimo é de R$998.00")
ir = 0
inss = 0
if (salario >= 1903.99) and (salario <= 2826.65):
    ir = (salario*7.5)/100
elif (salario >= 2826.66) and (salario <= 3751.05):
    ir = (salario*15)/100
elif (salario >= 3751.06) and (salario <= 4664.68):
    ir = (salario*22.5)/100
elif (salario > 4664.68):
    ir = (salario*27.5)/100
else:
    ir = 0
if (salario >= 1751.82) and (salario <= 2912.72):
    inss= (salario*9)/100
elif (salario >= 2919.73) and (salario <= 5839.45):
    inss = (salario*11)/100
elif (salario > 5839.75):
    inss = 642.34
else:
    inss = (salario*8)/100
sali = (salario - ir) - inss
print('=================================================')
print('=================================================')
print("RE: ", RE)
print("NOME: ", nome)
print("Salário Bruto: R$", salario)
print("INSS: R$", inss)
print("IR: R$", ir)
print("Salario Líquido: R$", sali)
print('=================================================')
print('=================================================')