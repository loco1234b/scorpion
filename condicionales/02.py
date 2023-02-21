import os
os.system("cls")

unidades = int(input("ingrese las unidades: "))

if unidades <= 50:
    caramelo = 5
elif unidades >= 51 and unidades <=100:
    caramelo = 10
elif unidades >= 101:
    caramelo = 15

importe = unidades * 20

if importe > 701: descuento = 0.16 * importe
elif importe >=501 and importe < 700:
    descuento = importe * 0.14
elif importe <= 500: descuento = importe * 0.12

total = importe - descuento

print("el importe de la compra es: ",importe)
print("el descuento es: ",descuento)
print("el importe a pagar es: ",total)
print("caramelos obsequiados es: ",caramelo)
