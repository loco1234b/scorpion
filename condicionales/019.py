import os
os.system("cls")

print("escriba 1 para femenino")
print("escriba 2 para masculino")
genero = int(input("ingrese el genero de la persona: "))
edad = int(input("edad de la persona: "))

if genero == 1:
    print("femenino")
if edad <= 23:
    categoria = "FA"
else:
    categoria = "FB"
print("la categoria femenina es: ",categoria)
 

if genero == 2:
    print("masculino")
if edad <= 25:
     categoria1 = "MA"
else:
     categoria1 = "MB"
print("la categoria masculino es: ",categoria1)
 
