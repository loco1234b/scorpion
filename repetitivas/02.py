import os
os.system("cls")

n1 = int(input("ingresa el primer numero: "))
n2 = int(input("ingrese el segundo numero: "))


def multiplicar(n1,n2):
    if n2 == 0:
        return 0
    elif n2 == 1:
        return n1
    else:
        return n1 + multiplicar(n1,n2-1)
if __name__== "__main__":
    resultado = multiplicar(n1,n2)
    print(resultado)
