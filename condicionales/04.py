import os
os.system("cls")

practica1 = int(input("nota practica 1: "))
practica2 = int(input("nota practica 2: "))
practica3 = int(input("nota practica 3: "))

if practica3 >= 10 and practica3 <= 18:
    pract3 = practica3 + 2

promedio = (practica1 + practica2 + pract3) / 3

print(" el promedio es: ",promedio)
