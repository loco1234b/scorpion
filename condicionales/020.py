import os
os.system("cls")

a = int(input("ingrese el primer numero: "))
b = int(input("ingrese el segundo numero: "))
c = int(input("ingrese el tercer numero: "))

if a > b and a > c and b > c:
    print("los numeros estan en descendentes")
elif c > b and c > a and b > a:
    print("los numeros estan en ascendentes")
else:
    print("los numeros estan en desorden")

