import os
os.system("cls")

monto = int(input("el monto vendido es: "))

comision = monto * 0.09
sueldobruto = 500 + comision
descuento = sueldobruto * 0.11
sueldoneto = sueldobruto - descuento

print("la comision es: ",comision)
print("el sueldo bruto es: ",sueldobruto)
print("el descuento es: ",descuento)
print("el sueldo neto es: ",sueldoneto)
print()
