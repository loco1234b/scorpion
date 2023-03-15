import os
os.system("cls")

numero = int(input("ingrese el numero de 4 cifras: "))

if numero >= 1000 and numero <= 9999:
    print("el numero es de 4 cifras")
else:
    print("el numero no tiene 4 cifras")
millar = numero / 1000
centena = (numero % 1000) /100
decena = (numero % 1000) % 100 / 10
unidad = (numero % 1000 % 100) % 10

mayor = max(millar,centena,decena,unidad)
menor = min(millar,centena,decena,unidad)
max =int(mayor)
min= int(menor)
print(f'el numero mayor es',max)
print(f'el numero menor es',min)
print(f'el mayor numero formado es = {max}{min}' )

