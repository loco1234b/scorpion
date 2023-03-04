import os
os.system("cls")

numero = int(input("ingresa el numero: "))
multiplos =int(input("ingrese los multiplos: "))

for i in range(numero,(numero * multiplos)+ 1,numero):
    print(str(i))
   