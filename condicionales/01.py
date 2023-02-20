import os
os.system("cls")

unidades =int(input("unidades: "))

if unidades <= 25:
    preciou = 27
elif unidades >= 26 and unidades <=50:
    preciou = 25
elif unidades >= 51:
    preciou = 23

importe = unidades * preciou

if unidades > 50: descuento = 0.15 * importe
else: descuento = 0.05 * importe

total = importe - descuento

print("el importe de la compra es: ",importe)
print("el descuento es: ",descuento)
print("el importe a pagar es: ",total)
print()