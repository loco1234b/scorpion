import os
os.system("cls")

monto = int(input("el monto vendido es: "))

sueldobasico = 250
if monto <=5000:
    comision = monto * 0.05
if monto >= 5001 and monto <= 10000:
    comision = monto *  0.08
if monto >= 10001 and monto <= 20000:
    comision = monto * 0.10
if monto >=20001:
    comision = monto *  0.15

sueldobruto = sueldobasico + comision

if sueldobruto >= 3500:
    descuento = sueldobruto * 0.15
elif sueldobruto <= 3499:
    descuento = sueldobruto * 0.08

sueldoneto = sueldobruto - descuento

print("la comision es: ",comision)
print("el sueldo bruto es: ",sueldobruto)
print("el descuento es: ",descuento)
print("el sueldo neto es : ",sueldoneto)

