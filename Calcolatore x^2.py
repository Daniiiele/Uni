import math
a=float(input("A:"))
b=float(input("B:"))
c=float(input("C:"))
print(f"{a} x^2 + {b} x + {c} =0")
delta=b**2-4*a*c
if  delta>0:
    print("Soluzioni X1=X2")
    X1=(-b+math.sqrt(delta))/2*a
    X2=(-b-math.sqrt(delta))/2*a
    print(X1)
    print(X2)
elif delta==0:
    print("Due soluzioni uguali X")
    X3=(-b+math.sqrt(delta))/2*a
    print(X3)
else:
    print("Error Δ<0")