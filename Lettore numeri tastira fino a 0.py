a=int(input("numeri:"))
Somma=0; count=0; max=a; min=a
while a!=0:
    if a>max:
        max=a
    if a<min:
        min=a
    count+=1
    Somma+=a
    a=int(input("numeri:"))
print("somma=",Somma)
media=Somma/count
print("Media=",media)
print("Max=",max)
print("Min=",min)
Var=Somma/count-media**2
print("varianza=",Var)