import os
os.system("cls")

numero = int(input("ingrese el numero: "))

i =numero
if numero % i ==0 and numero % 2 !=0 and numero % 3!=0:
    print(" es numero primo")
else:    
    print("el numero no es primo")
    