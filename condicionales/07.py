import os
os.system("cls")

numero1 = int(input("numero entero 1: "))
numero2 = int(input("numero entero 2: "))
numero3 = int(input("numero entero 3: "))

if numero1 > numero2:
    numeromedio = numero1
    x1 = numero2

else:
    numeromedio = numero2
    x1 = numero1
if numeromedio > numero3:
    numeromedio = numero3
if numeromedio < x1:
    numeromedio = x1

print("el numero medio es: ",numeromedio)
