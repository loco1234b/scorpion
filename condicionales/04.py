import os
os.system("cls")

pract1 = int(input("nota practica 1: "))
pract2 = int(input("nota practica 2: "))
pract3 = int(input("nota practica 3: "))

if pract3 >= 10:
    pract3 = pract3 + 2

promedio = (pract1 + pract2 + pract3) / 3

print(" el promedio es: ",promedio)
