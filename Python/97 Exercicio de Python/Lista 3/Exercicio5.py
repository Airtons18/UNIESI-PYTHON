x = 0
while x <1:
    a = int(input("População de A: "))
    b = int(input("População de B: "))
    ano = 0
    while a <= b:
        a += a * 0.03
        b += b * 0.015
        ano += 1
    print ( "A ultrapassa ou iguala a B em %d anos" %ano )
    r = int(input("Repetir? digite 1 ou aperte outro número para sair "))
    if r != 1:
        x = 1