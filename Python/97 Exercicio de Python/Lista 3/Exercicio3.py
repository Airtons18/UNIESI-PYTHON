x = 0
while x < 1:
    nome = input("Nome: ")
    nn = len(nome)
    if len(nome) > 3:
        idade = int(input("Idade: "))
        if (idade >= 0) and (idade <= 150):
            salario = float(input("Salario: "))
            if salario > 0:
                sexo = input("Sexo: ")
                if sexo == "m" or sexo == "f":
                    ec = input("Estado Civil: ")
                    if ec == "s" or ec == "c" or ec == "v" or ec == "d":
                        print("Todos os Dados são Valido!")
                        x = 1
                    else:
                        print("Estado Civil Invalido!")
                else:
                    print("Sexo Invalido!")
            else:
                print("Salario Invalido!")
        else:
            print("Idade Invalida!")
    else:
        print("Nome Invalido!")
