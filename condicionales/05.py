import os
os.system("cls")

numero = int(input("ingrese el numero de 4 cifras: "))

millar = numero / 1000
centena = (numero % 1000) /100
decena = (numero % 1000) % 100 / 10
unidad = (numero % 1000) % 100 % 10

mayor = millar
if (centena > mayor):
    mayor = centena
if (decena > mayor):
    mayor = decena
if (unidad > mayor):
    mayor = unidad

menor = millar

if (centena < menor):
    menor = centena
if (decena < menor):
    menor = decena
if (unidad < menor):
    menor = unidad

mayornum = mayor * 10 + menor
print("el numero mayor es: ", mayor)
print("el numero menor es: ", menor)
print("el numero mayor posible es: ",mayornum)

