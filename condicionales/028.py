import os
os.system("cls")

hora = int(input("ingrese la hora: "))



if hora > 23:
    print("error de hora")

if hora > 11:
    print("pm")
else:
    print("am")

if hora > 12:
    hora = hora - 12
