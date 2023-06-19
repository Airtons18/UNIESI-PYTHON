cont = False
while (cont == False):
    a = float(input("Valor de A: "))
    b = float(input("Valor de B: "))
    c = float(input("Valor de C: "))
    delta = (b**2-4*a*c)
    print("Delta = ", delta)
    if (delta < 0):
        print("Delta < 0, a equação não possui raiz real.")
    elif (delta > 0):
        delta = delta**(1/2)
        r1 = (-b-delta)/(2*a)
        r2 = (-b+delta)/(2*a)
        if (r1 == r2):
            print(r1)
        else:
            print(r1, "e", r2)
    elif (delta == 0):
        delta = delta**(1/2)
        r1 = (-b-delta)/(2*a)
        r2 = (-b+delta)/(2*a)
        if r1 == r2:
            print(r1)
        else:
            print(r1, "e", r2)
    sn = 0
    while sn == 0:
        vr = int(input("Deseja continuar |  SIM = [1]  ||  NÃO [2] : "))
        if (vr >= 1) and (vr <= 2):
            sn+= 1
            #if (vr == 1):
                #cont = False
            #else:
                #cont = True
        elif (vr == " " ):
            print("Digite 1= SIM ou 2= NÃO !!!: ")
        else:
            print("Digite 1= SIM ou 2= NÃO !!!: ")
        if (vr == 1):
            cont = False
        else:
            cont = True
            print("FIM")