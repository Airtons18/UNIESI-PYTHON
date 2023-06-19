L = []
z = False
x = 0 
while z == False:
    L.append('')
    L[x] = float(input('Digite um número: '))
    x += 1
    op = input('Deseja Continuar? S/N: ')
    if op == 'N' or op == 'n':
        z = True
L.sort()
print(L)