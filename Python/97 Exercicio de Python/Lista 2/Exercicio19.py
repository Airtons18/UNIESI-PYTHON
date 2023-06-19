n = input("digite um numero menor que 1000 ---> ")
nStr = str(n)
qtn = len(nStr)

if qtn == 3:
    centena = nStr[0:1]
    dezena = nStr[1:2]
    unidade = nStr[2:3]
    print(nStr+" = "+centena+" centenas , "+dezena+" dezenas, "+unidade+ " unidades")

if qtn == 2:
    dezena = nStr[0:1]
    unidade = nStr[1:2]
    print(nStr+" = "+dezena+" dezenas, "+unidade+ " unidades")

if qtn == 1:
    unidade = nStr[0:1]
    print(nStr+" = "+unidade+ " unidades")