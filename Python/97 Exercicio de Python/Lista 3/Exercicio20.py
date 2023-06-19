x = 0
vv = 0
while x < 1:
    while vv < 1:
        numero = int(input("Fatorial de: ") )
        if numero <= 16 and numero >= 0:
            vv+=1
        else:
            print("Erro")
        resultado=1
        count=1
        while count <= numero:
            resultado *= count
            count += 1
            x+=1
    print(resultado)