n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
op = int(input("Escolha um Operador: [-] = 0 | [+] = 1 | [/] = 2 | [*] = 3 | [**] = 4 | -> "))
if op == 0:
    s = n1-n2
elif op == 1:
    s = n1+n2
elif op == 2:
    s = n1/n2
elif op == 3:
    s = n1*n2
elif op == 4:
    s = n1**n2
if(s // 1 == s):
    print("numero inteiro")
else:
    print("Numero Decimal")
par = s%2
if par == 0:
    print("O número", s, "é PAR")
else: 
    print("O número", s, "é IMPAR")
if s > 0:
    print("Número POSITIVO")
elif s < 0:
    print("Número NEGATIVO")
else:
    print("Número NEUTRO")