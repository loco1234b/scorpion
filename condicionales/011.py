import os
os.system("cls")

numero = int(input("ingresa el numero : "))

if numero > 0:
    print("el numero es positivo ", "+" ,numero)

elif numero < 0:
    print("el numero es negativo ",numero)

elif numero == 0:
    print("el numero es cero o neutro")