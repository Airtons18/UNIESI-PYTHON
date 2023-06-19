p1 = float(input("Produto 1 preço: R$"))
p2 = float(input("Produto 2 preço: R$"))
p3 = float(input("Produto 3 preço: R$"))
L = [p1, p2, p3]
maisbarato =  min(L)
print("O produto mais barato é R$", maisbarato)