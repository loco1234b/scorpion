import os
os.system("cls")

numero = int(input("ingrese el numero: "))

def primo(numero):
    for i in range(2,numero):
        if numero % i ==0:
            print("no es numero primo")
            return False
    print("el numero es primo")
    return True