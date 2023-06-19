#Quest�o09
print("Questão 09")
def escola():
    numAlunos=int(input("Digite a quantidade de alunos: "))
    RE=[]
    notas=[]
    med=[]
    acum=0
    x=0
    y=0
    z=0
    cnt=1
    subst=0
    while(x<numAlunos):
        RE.append("")
        RE[x]=int(input("Digite o RE do aluno: "))
        subst=float(input("Digite a nota do aluno: "))
        notas.append(subst)
        x+=1
        y+=1
        acum+=subst
        while(cnt<=3):
            subst=float(input("Digite a nota do aluno: "))
            notas.append(subst)
            acum+=subst
            y+=1
            cnt+=1
        cnt=1
        med.append("")
        med[z]=acum/4
        z+=1
    percRE=0
    percNt=0
    while(percRE<numAlunos):
        bo=False
        contar=1
        print("<---------------------------------------------------->")
        print("RE do aluno:",RE[percRE])
        print("Média do aluno:",med[percRE])
        if(med[percRE]>=7):
            print("Situação: Aprovado!")
        else:
            print("Situação: Exame!")
        percRE+=1
        while(bo==False):
            if(contar==4):
                bo=True
            print("Nota",contar,"do aluno:",notas[percNt])
            contar+=1
            percNt+=1
        print("<---------------------------------------------------->")
escola()