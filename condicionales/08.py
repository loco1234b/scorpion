import os
os.system("cls")

examen1 = int(input("examen 1 : "))
examen2 = int(input("examen 2 : "))
examen3 = int(input("examen 3 : "))

propina = 20

if examen1 > 10:
    propina += 5

if examen2 > 10:
    propina += 5

if examen3 > 10:
    propina += 5

print("monto total de la propina: ",propina)
