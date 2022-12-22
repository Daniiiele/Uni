def leggiMatr(name,x):
    m=[]
    for riga in range (0,x):
        l=[]
        for col in range(0,x):
            l.append(int(input(f"{name}[{riga}][{col}]:")))
        m.append(l)
    return m

def stampaMat(m):
    for riga in range(0, len(m)):
        for col in range(0, len(m[riga])):
            print(m[riga][col], end="\t")
        print()

def prodMat(m1,m2):
    m3=[]
    for riga in range(0, len(m1)):
        m3.append([])
        for col in range(0, len(m2[riga])):
            m3[riga].append(0)
            for z in range(0, len(m1[riga])):
                m3[riga][col]+=m1[riga][z]*m2[z][col]
    return m3

x=int(input("quante righe?:")); y=x
m1=leggiMatr("m1:",x)
m2=leggiMatr("m2:",x)
stampaMat(m1)
print()
stampaMat(m2)
print()
stampaMat(prodMat(m1,m2) )