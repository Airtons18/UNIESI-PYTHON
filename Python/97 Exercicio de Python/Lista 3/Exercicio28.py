qtcds = int(input("Digite a quantidade de CD's : "))
cds = []
n_cd = 1

for i in range(qtcds):
    print("CD número ", n_cd)
    vdc = cds.append(float(input("Digite o valor do CD: ")))
    n_cd += 1

m = sum(cds) / len(cds)
print("A media para cada CD é: ", m)