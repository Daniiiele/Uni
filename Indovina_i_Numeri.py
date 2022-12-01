import random
n=random.randint(0,100)
print(n)
t=5
b,c=0,100
while t!=0:
    t=t-(1)
    a=int(input("Inserischi un numero ="))
    if a>n:
        print("Il numero è più basso di",a)
        print("-Riprova hai ancora",t,"tentativi")
    elif a<n:
        print("Il numero è più alto di",a)
        print("-Riprova hai ancora",t,"tentativi")
    else:
        t=0
        print("Hai indovinato")
#parte extra(bonus)
    if n!=a:
        if a<b and a<n and t!=4:
            print("Ti ho detto che è più alto di", b)
        elif  a>c and a>n and t!=4:
            print("Ti ho detto che è più basso di", c)
        elif a<n and b<a:
            b=a
        elif a>n and c>a:
            c=a
        else:
            print("probblema")
