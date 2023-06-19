dia = int(input("Dia correspodente: "))
D = {1:'Domingo', 2:'Segunda', 3:'Terça', 4:'Quarta', 5:'Quinta', 6:'Sexta', 7:'Sábado'}
verif = dia in D
if verif == True:
    if dia == 1:
        print(D[1])
    elif dia == 2:
        print(D[2])
    elif dia == 3:
        print(D[3])
    elif dia == 4:
        print(D[4])
    elif dia == 5:
        print(D[5])
    elif dia == 6:
        print(D[6])
    elif dia == 7:
        print(D[7])
else:
    print("Valor Inválido!")