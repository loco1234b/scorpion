import os
os.system("cls")

unidades = int(input("ingrese el numero de unidades: "))
codigo = int(input("ingrese el codigo: "))

if codigo == 101:
    precio = 17
elif codigo == 102:
    precio = 25
elif codigo == 103:
    precio = 16
elif codigo == 104:
    precio = 27

importecompra = precio * unidades

if unidades < 10:
    descuento = importecompra * 0.05
if unidades > 11 and unidades < 20:
    descuento = importecompra * 0.08
if unidades > 21 and unidades < 30:
    descuento = importecompra * 0.10
if unidades > 31:
    descuento = importecompra * 0.13

total_a_pagar = importecompra - descuento

print("el importe de la compra es: ",importecompra)
print("el descuento es: ",descuento)
print("el total a pagar es: ",total_a_pagar)
