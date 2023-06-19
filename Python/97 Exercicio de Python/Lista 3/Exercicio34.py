n = int(input("Digite um número: "))
cont = 0
for i in range(n):
    if n%(i+1) == 0:
        cont+=1
    else:
        cont
if cont == 2:  
    print("O número", n, "é primo")
else:
    print("O número", n, "não é primo")