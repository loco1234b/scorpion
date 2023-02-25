import os
os.system("cls")

unidades = int(input("ingrese la cantidad de docenas del producto: "))
precio = int(input("el precio de la docena es: "))

montocompra = unidades * precio
if unidades >= 6:
    descuento = montocompra * 0.15 
elif unidades <= 5:
    descuento = montocompra * 0.10

total = montocompra - descuento

if unidades >= 30 :
    obsequio = 2 * (unidades / 3)
else:
    obsequio = 0

print("el monto de la compra es : ",montocompra)
print("el descuento es : ",descuento)
print("el total a pagar es: ",total)
print("la cantidad de lapiceros obsequiados es: ",obsequio)