h=float(input("Peso,Kg:"))
p=float(input("Altezza,m:"))
I=h/(p**2)
print("%.2f"%I)
if I<16.1:
    print("Grave magrezza")
elif 16.1==I or I<=17.50:
    print("Sottopeso")
elif 17.51==I or I<=18.50:
    print("Leggermente sottopeso")
elif 18.51==I or I<=25.00:
    print("Regolare")
elif 25.01==I or I<=30.00:
    print("Sovrappeso")
elif 30.01==I or I<=35.00:
    print("Obesità di I classe (moderata)")
elif 35.01==I or I<=40.00:
    print("Obesità di II classe (grave)")
else I>40.00:
    print("Obesità di III classe (gravissima)")
