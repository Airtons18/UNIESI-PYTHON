n_temperaturas = int(input("Quantidade de temperaturas que irá digitar: "))
temp = []
n_temperatura = 1
for i in range(n_temperaturas):
    print("Temperatura n° ", n_temperatura)
    temperatura = temp.append(float(input("Digite a temperatura: ")))
    n_temperatura += 1

print("Maior temperatura = ", max(temp))
print("Menor temperatura = ", min(temp))
print("Média = ", round(sum(temp) / len(temp), 2))