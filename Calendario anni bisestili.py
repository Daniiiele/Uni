a=int(input("Anno:")) #immetti anno
#metodo A
if(a%4 != 0):
    print("Anno non Bisestile")
elif(a%100!=0):
    print("Anno Bisestile")
elif(a%400==0):
    print("Anno Bisestile")
else:
    print("Anno non Bisestile")
#matodo B non funziona
if a%4==0: #controlla divisibilita per4
    if a%100!=0:
        if a%400==0:
             print("Anno non Bisestile")
        else:
            print("Anno 1Bisestile")
    else:
        print("Anno2 Bisestile")
else:
    print("1Anno non Bisestile")
