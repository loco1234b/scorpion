import os
os.system("cls")

unidadesA = int(input("unidades del producto A: "))
unidadesB = int(input("unidades del producto B: "))

PRODUCTOA = unidadesA * 25
PRODUCTOB = unidadesB * 30

if unidadesA >= 50:
    descuentoa = PRODUCTOA * 0.15
else:
    descuentoa = 0

if unidadesB >= 60:
    descuentob = PRODUCTOB * 0.10
else:
    descuentob = 0

importebruto = PRODUCTOA + PRODUCTOB
descuentotal = descuentoa + descuentob
totalpagar = importebruto - descuentotal

print("el importe bruto es: ",importebruto)
print("el descuento es: ",descuentotal)
print("el total a pagar es: ",totalpagar)
