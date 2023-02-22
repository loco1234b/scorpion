import os,math
os.system("cls")

edad1 = int(input("ingrese la edad 1: "))
edad2 = int(input("ingrese la edad 2: "))
edad3 = int(input("ingrese la edad 3: "))

edadmayor = max(edad1,edad2,edad3)
edadmenor = min(edad1,edad2,edad3)

print("la edad mayor es: ",edadmayor)
print("la edad menor es: ",edadmenor)
