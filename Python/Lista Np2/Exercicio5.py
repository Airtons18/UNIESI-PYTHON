def positivo():
    if(n>0):
        print("O número",n," e a soma de seus divisores",somaDivisores())
    return(x)
def somaDivisores():
    c = 1
    a = 0
    while c < n:
        if((n%c)==0):
            a += c
        c += 1
    return( a )
i = 1
global n
while i <= 5:
    n = int(input("Digite um número: "))
    i += 1
    positivo()
