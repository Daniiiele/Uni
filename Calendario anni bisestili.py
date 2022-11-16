a = int(input("Anno:"))  #immetti anno
#metodo A
if (a % 4 != 0):
  print("Anno non Bisestile")
elif (a % 100 != 0):
  print("Anno Bisestile")
elif (a % 400 == 0):
  print("Anno Bisestile")
else:
  print("Anno non Bisestile")
#metodo B
if a % 4 == 0:  #controlla divisibilita per4
  if a % 400 != 0:
    if a % 100 == 0:
      print("Anno non Bisestile")
    else:
      print("Anno Bisestile")
  else:
    print("Anno Bisestile")
else:
  print("Anno non Bisestile")
#metodo C
if a % 4 == 0 and a % 400 == 0 or a % 100 != 0:
  print("Anno bisestile")
else:
  print("Anno non bisestile")


