import os
os.system("cls")

metros = int(input("ingrese la cantidad de metros: "))

cent = metros * 100
pulg = cent * 2.54
pie = pulg / 12
yardas = pie / 3

print("la cantidad es ",cent,"centimetros")
print("la cantidad es ",pulg,"pulgadas")
print("la cantidad es ",pie,"pie")
print("la cantidad es ",yardas,"yardas")
print()