x = 0
while x < 1:
    tab = int(input("Tabuada do: "))
    inicia = int(input("Começar do: "))
    termina = int(input("Até: "))
    termina = termina+1
    if inicia > termina:
        print("Inicio Maior que o FIM!!")
    else:
        x = 1
for inicia in range(inicia, termina, 1):
    print(inicia, "X", tab, "=", inicia*tab)