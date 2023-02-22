import os

os.system("cls")

pies = int(input("ingresa la cantidad de pies: "))
pulgadas = int(input("ingresa la cantidad de pulgadas: "))

cm = pies * 30.48
cm += pulgadas * 2.54
metro = cm / 100

print("su estatura es: ",metro,"m")
print()