qletra = input("Digite uma Letra: ")
L = ["A", "E" ,"I" ,"O" , "U", "a", "e", "i", "o", "u"]
vsn = qletra in L
if vsn == True:
    print("A letra", qletra, "é uma vogal !")
else:
    print("A letra", qletra, "é uma consoante !")