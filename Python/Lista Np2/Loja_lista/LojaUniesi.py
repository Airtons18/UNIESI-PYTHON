import os

#MENU
def menu():
    print("================ LOJA UNIESI =================")
    print("| Selecione a opção a seguir....             |")
    print('|    1 - Comprar                             |')
    print('|    2 - Lista de Compra                     |')
    print("|    3 - Remover Item                        |")
    print("|    4 - Fechar Compra                       |")
    print("|    5 - Sair                                |")
    print("==============================================")

#Remover Itens
def remover(l1, l2, l3, l4, idd):
    del l1[idd]
    del l2[idd]
    del l3[idd]
    del l4[idd]
    l1[idd].append(" ")
    l2[idd].append(" ")
    l3[idd].append(" ")
    l4[idd].append(" ")
    for p in range(idd, len(l1), 1):
        q = p+1
        l1[p] = l1[q]
        l2[p] = l2[q]
        l3[p] = l3[q]
        l4[p] = l4[q]
#Opções do Menu
Ln = []
Lv = []
Lq = []
Lt = []
g = 0

z = False
while z != True:
    menu()
    resp = int(input('Digite a Opção Desejada --> ' ))
    if resp == 1:
        b = False
        Ln.append('')
        Lv.append('')
        Lq.append('')
        Lt.append('')
        while b == False:
            Ln[g] = input('Nome do Produto: ')
            if len(Ln[g]) > 0:
                b = True
        b = False
        while b == False:
            Lv[g] = float(input('Valor da unidade: '))
            if Lv[g] > 0:
                b = True
        b = False
        while b == False:
            Lq[g] = int(input('Quantidade do Produto: '))
            if Lq[g] > 0:
                b = True
        os.system('cls' if os.name == 'nt' else 'clear')
        Lt[g] = Lv[g]*Lq[g]
        print(Ln[g], "valor unidade R$", Lv[g], "quantia adicionada", Lq[g], "valor total R$", Lt[g])
        g += 1
    elif resp == 2:
        for i in range(0, g, 1):
            print(i, '---', Ln[i], "valor unidade R$", Lv[i], "quantia adicionada", Lq[i], "valor total R$", Lt[i])
    elif resp == 3:
        rem = int(input("Digite o ID do Produto para Remover: "))
        #remover(Ln, Lv, Lq, Lt, rem)
        del Ln[rem]
        del Lv[rem]
        del Lq[rem]
        del Lt[rem]
        g -= 1
    elif resp == 4:
        print("=========== FECHAMENDO DA COMPRA =============")
        print("|  Numero de Produtos: ", g)
        print("|  Quntidade total de produtos: ", sum(Lq))
        print("|  Valor Total dos Produtos: ", sum(Lt))
        Ln = []
        Lv = []
        Lq = []
        Lt = []
        g = 0

    elif resp == 5:
        print("Loja Encerrada *-*")
        z = True