"""tre pioli A,B,C, n dischi, devo spostare la piramide di dischi da un piolo e riprodurlo in un altro piolo,
 posso spostare un solo disco alla volta, non posso mettere un disco grande su un disco piccolo,
torre di 4 dischi, tre pilo, da pioli A a pilo B: sposto i primi 3 dischi nel piolo B e l'ultimo lo sposto su C, e i dischi in B li sposto in C
              se n=1 ---> (da->a)
H(n,da,a,per):
              se n>1  |H(n-1,da,per,a)|
                      |H(1,da,a,per)  |
                      |H(n-1,per,a,da)|"""


def hanoi(n,da,a,per):
    if n==1:
        print(f"{da} -> {a}")
        return 1
    else:
        return hanoi(n-1,da,per,a)+hanoi(1,da,a,per)+hanoi(n-1,per,a,da)

nmosse=hanoi(int(input("n dischi:")),"A","C","B")
print(f"ho fatto {nmosse} mosse")