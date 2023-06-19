x = 0
while (x <= 1):
        nome = input("Nome do Aluno: ")
        np1 = float(input("Nota Np1: "))
        np2 = float(input("Nota Np2: "))
        media = (np1+np2)/2
        if (media < 7):
            rfinal = "REPROVADO"
        else:
            rfinal = "APROVADO"    
        print("O aluno ", nome, "teve a média de ", media, "e foi", rfinal)
        x= int(input("1 - Continuar  | 2 - Cancelar | --> "))