import os
os.system("cls")

numero = int(input("ingrese el numero: "))

for f in range(1,13):
    multiplicacion = numero * f
    print(f'{numero} x {f} = {multiplicacion}')