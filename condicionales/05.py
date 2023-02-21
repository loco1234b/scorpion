import os
os.system("cls")

numero = int(input("ingrese el numero de 4 cifras: "))

mill = numero / 1000
cent = (numero % 1000) /100
dece = (numero % 1000) % 100 / 10
unid = (numero % 1000) % 100 % 10

mayor = mill
if (cent > mayor):
    mayor = cent
if (dece > mayor):
    mayor = dece
if (unid > mayor):
    mayor = unid

menor = mill

if (cent < menor):
    menor = cent
if (dece < menor):
    menor = dece
if (unid < menor):
    menor = unid

mayornum = mayor * 10 + menor
print("el numero mayor es: ", mayor)
print("el numero menor es: ", menor)
print("el numero mayor posible es: ",mayornum)

