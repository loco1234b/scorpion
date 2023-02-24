import os
os.system("cls")

numero = int(input("el numero de la tarjeta es: "))
monto = int (input("el precio es: "))

importecompra = monto

if numero % 2 ==0 and numero > 100:
    print("el numero es par 0.15")
    descuento = importecompra * 0.15
else:
    print("el numero es impar 0.05")
    descuento = importecompra * 0.05

importetotal = importecompra - descuento

print("el numero de la tarjeta es: ",numero)
print("el descuento es: ",descuento)
print("el importe de la compra es: ",importetotal)
