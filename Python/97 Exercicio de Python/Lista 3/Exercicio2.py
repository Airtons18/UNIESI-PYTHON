x = 0
while x < 1:
    u = input("Usuario: ")
    s = input("Senha: ")
    if u != s:
        print("Sucesso")
    else:
        print("Erro senha não pode ser igual ao usuario:")