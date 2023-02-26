import os
os.system("cls")

monto = int(input("el monto vendido es: "))

comision = monto * 0.15
sueldobasico = 600
sueldobruto = sueldobasico + comision

if sueldobruto >= 1800:
    descuento = sueldobruto * 0.10
else:
    descuento = sueldobruto * 0.05

if monto >= 1000:
    polos = 3
else:
    polos = 1
sueldoneto = sueldobruto - descuento

print("el sueldo bruto es: ",sueldobruto)
print("el descuento es: ",descuento)
print("el sueldo neto es : ",sueldoneto)
print("el numero de polos obsequiados es: ",polos)