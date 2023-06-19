data = input("dd/mm/aaaa: ")
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

vld = 1
x = 0
while vld == 1 and x == 0:
    if (ano%4 == 0 and ano%100!= 0) or ano%400 == 0:
        bissexto = 1
    else:
        bissexto = 0
    if mes < 1 or mes > 12:
        vld = 0
    if dia > 31 or ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30):
        vld = 0
    if (mes == 2 and bissexto == 0 and dia > 28) or ( mes == 2 and bissexto == 1 and dia > 29):
        vld = 0
    x+= 1
if vld == 1:
    print("data valida")
else:
    print("data invalida")