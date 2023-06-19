arqmb = float(input("Digite o tamanho do arquivo em MB: "))
vinter = float(input("Velocidade da Internet: "))
vinter = vinter/8
vdown = arqmb/vinter
tempo = vdown/60
print("A Velocidade de download em minutos são: ", '{:.2f}'.format(tempo))