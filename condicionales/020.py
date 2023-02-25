import os
os.system("cls")

a = int(input("ingrese el primer numero: "))
b = int(input("ingrese el segundo numero: "))
c = int(input("ingrese el tercer numero: "))

if a > c :
    print("los numeros estan en ascendentes")
elif c < a:
    print("los numeros estan son descendentes")
else:
    print("los numeros estan en desorden")

