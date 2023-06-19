L = []
for x in range(1 , 11, 1):
    n = int(input("\nDigite o número: "))
    L.append(n)
par = 0
impar = 0

for value in L:
    if value % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print("Par: ", par, "\nImpar: ", impar)