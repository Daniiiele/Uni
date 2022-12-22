def leggilista(nome):
    v=[]
    x=int(input(nome +":"))
    while len(v)==0 or x>=v[-1]:
        v.append(x)
        x = int(input(nome +":"))
    return v

#calcolo
v1=leggilista("v1")
v2=leggilista("v2")

def fondi(v1,v2):
    v3=[];i1,i2=0,0
    while i1 < len(v1) or i2 < len(v2):
        if i2 == len(v2) or i1 < len(v1) and v1[i1] < v2[i2]:
            v3.append(v1[i1])
            i1 += 1
        else:
            v3.append(v2[i2])
            i2 += 1
    return v3

v3=fondi(v1,v2)

"""
v3=[] ; i1,i2=0,0
while i1<len(v1) and i2<len(v2):
    if v1[i1]<v2[i2]:
        v3.append(v1[i1])
        i1+=1
    else:
        v3.append(v2[i2])
        i2+=1
while i1 < len(v1):
    v3.append(v1[i1])
    i1 += 1
while i2 < len(v2):
    v3.append(v2[i2])
    i2 += 1
"""


#printing
print("v1:",v1)
print("v2:",v2)
print("v3:",v3)
