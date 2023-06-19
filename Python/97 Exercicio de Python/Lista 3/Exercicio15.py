#1,1,2,3,5,8,13,21,34,55
p1 = 1
p2 = 1
cont  = 1
print(p1)
while cont < 7:
    p1 = p1 + p2
    print(p1)
    p2 = p1 + p2
    print(p2)
    cont+=1