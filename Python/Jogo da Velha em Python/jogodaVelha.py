'''
@Author: Airton Aparecido dos Santos Neto
'''



import os

def tabela(a, b, c, d, e, f, g, h, i):
    print('_'+a+'_|_'+b+'_|_'+c+'_\n' '_'+d+'_|_'+e+'_|_'+f+'_\n' '_'+g+'_|_'+h+'_|_'+i+'_')

global vez

def vervez(vez):
    if vez == 'x':
        vez = 'o'
    else:
        vez = 'x'
    return vez

pos1 = '_'
pos2 = '_'
pos3 = '_'
pos4 = '_'
pos5 = '_'
pos6 = '_'
pos7 = '_'
pos8 = '_'
pos9 = '_'
ok = False

P = [11, 12, 13, 21, 22, 23, 31, 32, 33]
vez = input('Quem começa? ')
while (ok == False):
    tabela(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9)
    posicao = int(input('Que Posição? '))
    if posicao == 11:
        pos1 = vez
        vez = vervez(vez)
        if posicao in P == True:
            #os.system('cls' if os.name == 'nt' else 'clear')
            P.remove(posicao)
    elif posicao == 12:
        pos2 = vez
        vez = vervez(vez)
        if posicao in P == True:
            #os.system('cls' if os.name == 'nt' else 'clear')
            P.remove(posicao)
    elif posicao == 13:
        pos3 = vez
        vez = vervez(vez)
        if posicao in P == True:
            #os.system('cls' if os.name == 'nt' else 'clear')
            P.remove(posicao)
    elif posicao == 21:
        pos4 = vez
        vez = vervez(vez)
        if posicao in P == True:
            #os.system('cls' if os.name == 'nt' else 'clear')
            P.remove(posicao)
    elif posicao == 22:
        pos5 = vez
        vez = vervez(vez)
        if posicao in P == True:
            #os.system('cls' if os.name == 'nt' else 'clear')
            P.remove(posicao)
    elif posicao == 23:
        pos6 = vez
        vez = vervez(vez)
        if posicao in P == True:
            #os.system('cls' if os.name == 'nt' else 'clear')
            P.remove(posicao)
    elif posicao == 31:
        pos7 = vez
        vez = vervez(vez)
        if posicao in P == True:
            #os.system('cls' if os.name == 'nt' else 'clear')
            P.remove(posicao)
    elif posicao == 32:
        pos8 = vez
        vez = vervez(vez)
        if posicao in P == True:
            #os.system('cls' if os.name == 'nt' else 'clear')
            P.remove(posicao)
    elif posicao == 33:
        pos9 = vez
        vez = vervez(vez)
        if posicao in P == True:
            #os.system('cls' if os.name == 'nt' else 'clear')
            P.remove(posicao)
    if (pos1 != '_' and pos2 != '_' and pos3 != '_' and pos4 != '_' and pos5 != '_' and pos6 != '_' 
    and pos7 != '_' and pos8 != '_' and pos9 != '_'):
        tabela(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9)
        ok = True
    if (pos1 and pos2 and pos3 == 'x' or pos4 and pos5 and pos6 == 'x' or pos7 and pos8 and pos9 == 'x' or
    pos1 and pos4 and pos7 == 'x' or pos2 and pos5 and pos8 == 'x' or pos3 and pos6 and pos9 == 'x' or
    pos1 and pos5 and pos9 == 'x' or pos3 and pos5 and pos7):
        print('X é o Vencedor')
