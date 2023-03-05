import os
os.system("cls")

numero = int(input("ingrese el numero: "))

if numero % 1 ==0 and numero % numero ==0:
    print("el numero es primo")
else:
    print("el numero no es primo")