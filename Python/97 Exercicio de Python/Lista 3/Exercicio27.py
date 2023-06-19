tm = int(input("Quantas turmas? : "))
at = []
t = 1

for i in range(tm):
    print("turma ", t)
    a = int(input("Alunos da turma : "))
    while a > 40:
        print("turma ", t, " [uma turma só pode ter 40 alunos]")
        a = int(input("Alunos da turma : "))
    t += 1
    at.append(a)

m = sum(at) / len(at)
print("A media e igual a: ", m)