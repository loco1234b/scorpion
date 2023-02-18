import os
os.system("cls")

monto = int(input("el monto vendido es: "))

comision = monto * 0.09
sueldobr = 500 + comision
descuento = sueldobr * 0.11
sueldone = sueldobr - descuento

print("la comision es: ",comision)
print("el sueldo bruto es: ",sueldobr)
print("el descuento es: ",descuento)
print("el sueldo neto es: ",sueldone)
print()
