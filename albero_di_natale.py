def ripeti(c,n):
    for i in range(0,n):
        print(c,end="")

def ramo(n):
    print("*",end="");ripeti("-",n)
    print("|",end="")
    ripeti("-",n);print("*")

def albero(r,spazi=0): #se ho ad esempio un albero largo 13 voglio che i rami siano preceduti da 8 spazi e lunghi 5
    if r==-1:
        ripeti(" ",spazi)
        print("+")
    else:
        albero(r-1, spazi+1)
        ripeti(" ", spazi); ramo(r)

albero(100,1)