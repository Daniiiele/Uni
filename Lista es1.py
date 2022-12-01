v=0
b=[]
while v!=100:
    x=int(input("valori:"))
    v+=x
    b.append(x)
print(b)
a=int(input("vecchio valore da cambiare:"))
c=int(input("nuovo valore:"))
p=0
for i in range (0,len(b)):
    if b[i]==a:
        b[i]=c
for i in b:
    print(b,end=" ")
