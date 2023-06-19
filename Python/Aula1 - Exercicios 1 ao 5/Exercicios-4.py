funcio = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))
porcen = float(input("Digite a porcentagem de aumento: "))
aumento = (salario * porcen) / 100
print("O novo salário do(a) ",funcio, "será de ",salario+aumento, "reais")
