import os
os.system("cls")

hora = float(input("ingrese la hora: "))

if hora <= 12:
    print(str(hora) + ": am")

else:
    print(str( hora - 12) + ": pm")


