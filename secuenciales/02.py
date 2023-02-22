import os

os.system("cls")

metros = int(input("ingrese la cantidad de metros: "))

centimetros = metros * 100
pulgadas = centimetros * 2.54
pie = pulgadas / 12
yardas = pie / 3

print("la cantidad es ",centimetros,"centimetros")
print("la cantidad es ",pulgadas,"pulgadas")
print("la cantidad es ",pie,"pie")
print("la cantidad es ",yardas,"yardas")
print()