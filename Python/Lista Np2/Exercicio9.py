re = []
n1=[]
n2=[]
n3=[]
n4=[]
def qtd_a(alunos):
	for i in range(0, alunos, 1):
		re.append("")
		n1.append("")
		n2.append("")
		n3.append("")
		n4.append("")
		re[i]=int(input("RE do Aluno: "))
		n1[i]=float(input("Nota 1: "))
		n2[i]=float(input("Nota 2: "))
		n3[i]=float(input("Nota 3: "))
		n4[i]=float(input("Nota 4: "))
alunos = int(input("Quantidade de Alunos: "))
qtd_a(alunos)
for i in range(0, alunos, 1):
	print("====================")
	print("Media do Aluno RE:",  re[i])
	print("Media: ", (n1[i]+n2[i]+n3[i]+n4[i])/4)
	media = (n1[i]+n2[i]+n3[i]+n4[i])/4
	if media >= 7.0:
		print("Aprovado")
	else:
		print("Exame")
	print("=================")